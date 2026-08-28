

import gradio as gr
from ultralytics import YOLO
import cv2
import tempfile
import os
import math

# =========================================================
# LOAD MODELS
# =========================================================

# Object detection + tracking
object_model = YOLO("yolo11n.pt")

# Pose model for human body position
pose_model = YOLO("yolo11n-pose.pt")


# =========================================================
# HELPER
# =========================================================

def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


# =========================================================
# VIDEO PROCESSING
# =========================================================

def process_video(video_path, confidence):

    if video_path is None:
        return None, "Please upload a video first."

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return None, "❌ Could not open video."

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Output file
    output_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp4"
    )

    output_path = output_file.name
    output_file.close()

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    # Track previous positions
    previous_positions = {}

    # Statistics
    max_people = 0
    max_vehicles = 0
    max_chairs = 0

    frame_number = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame_number += 1

        # =================================================
        # OBJECT DETECTION + TRACKING
        # =================================================

        results = object_model.track(
            frame,
            conf=confidence,
            tracker="bytetrack.yaml",
            persist=True,
            verbose=False
        )

        result = results[0]

        people = 0
        vehicles = 0
        chairs = 0
        moving = 0

        current_positions = {}

        if result.boxes is not None:

            boxes = result.boxes

            for i, box in enumerate(boxes):

                cls = int(box.cls[0])
                name = object_model.names[cls]

                confidence_score = float(box.conf[0])

                # Tracking ID
                track_id = None

                if box.id is not None:
                    track_id = int(box.id[0])

                # Bounding box
                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                # -----------------------------------------
                # PERSON
                # -----------------------------------------

                if name == "person":

                    people += 1

                    if track_id is not None:

                        current_positions[track_id] = (
                            center_x,
                            center_y
                        )

                        if track_id in previous_positions:

                            movement = distance(
                                previous_positions[track_id],
                                current_positions[track_id]
                            )

                            if movement > 8:
                                moving += 1

                # -----------------------------------------
                # VEHICLES
                # -----------------------------------------

                if name in [
                    "car",
                    "truck",
                    "bus",
                    "motorcycle",
                    "bicycle"
                ]:
                    vehicles += 1

                # -----------------------------------------
                # CHAIRS
                # -----------------------------------------

                if name == "chair":
                    chairs += 1

        previous_positions = current_positions

        # =================================================
        # POSE DETECTION
        # =================================================

        sitting = 0

        pose_results = pose_model(
            frame,
            conf=confidence,
            verbose=False
        )

        pose_result = pose_results[0]

        if pose_result.keypoints is not None:

            keypoints = pose_result.keypoints.xy

            for person_keypoints in keypoints:

                # COCO keypoints:
                # 5 = left shoulder
                # 6 = right shoulder
                # 11 = left hip
                # 12 = right hip
                # 13 = left knee
                # 14 = right knee

                try:

                    shoulder_y = (
                        float(person_keypoints[5][1]) +
                        float(person_keypoints[6][1])
                    ) / 2

                    hip_y = (
                        float(person_keypoints[11][1]) +
                        float(person_keypoints[12][1])
                    ) / 2

                    knee_y = (
                        float(person_keypoints[13][1]) +
                        float(person_keypoints[14][1])
                    ) / 2

                    # Simple posture heuristic
                    if (
                        knee_y > 0
                        and hip_y > 0
                        and shoulder_y > 0
                        and knee_y < hip_y * 1.8
                    ):
                        sitting += 1

                except:
                    pass

        # =================================================
        # STATISTICS
        # =================================================

        max_people = max(max_people, people)
        max_vehicles = max(max_vehicles, vehicles)
        max_chairs = max(max_chairs, chairs)

        standing = max(0, people - sitting)

        # =================================================
        # DRAW DASHBOARD ON VIDEO
        # =================================================

        annotated = result.plot()

        # Dashboard background
        cv2.rectangle(
            annotated,
            (10, 10),
            (330, 225),
            (20, 20, 20),
            -1
        )

        # Title
        cv2.putText(
            annotated,
            "AI MONITORING",
            (25, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Statistics
        stats = [
            f"People: {people}",
            f"Moving: {moving}",
            f"Sitting: {sitting}",
            f"Standing: {standing}",
            f"Vehicles: {vehicles}",
            f"Chairs: {chairs}"
        ]

        y = 70

        for text in stats:

            cv2.putText(
                annotated,
                text,
                (25, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            y += 25

        writer.write(annotated)

    cap.release()
    writer.release()

    # =====================================================
    # FINAL REPORT
    # =====================================================

    report = f"""
## 🎯 Detection Report

| Statistic | Result |
|---|---:|
| 👥 Maximum People Detected | {max_people} |
| 🚗 Maximum Vehicles Detected | {max_vehicles} |
| 🪑 Maximum Chairs Detected | {max_chairs} |
| 🎞️ Frames Processed | {frame_number} |

### 🤖 AI Models

- YOLO11 Object Detection
- YOLO11 Pose
- ByteTrack
- OpenCV
- Gradio
"""

    return output_path, report


# =========================================================
# GRADIO INTERFACE
# =========================================================

with gr.Blocks(
    title="AI People & Object Monitoring",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown(
        """
        # 🎯 AI People & Object Monitoring System

        ### YOLO11 + ByteTrack + Pose Estimation

        Upload a video and the system will detect, track and analyse
        people and objects.
        """
    )

    with gr.Row():

        # =================================================
        # LEFT SIDE
        # =================================================

        with gr.Column(scale=1):

            gr.Markdown("## 📊 Monitoring")

            people_display = gr.Markdown(
                """
                ### 👥 People
                Upload a video to begin analysis.
                """
            )

            gr.Markdown(
                """
                ### 📌 Available Analysis

                👥 People
                🚶 Moving
                🪑 Sitting
                🧍 Standing
                🚗 Vehicles
                🪑 Chairs
                🎯 Tracking IDs
                """
            )

            confidence = gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.5,
                step=0.05,
                label="🎯 Detection Confidence"
            )

        # =================================================
        # RIGHT SIDE
        # =================================================

        with gr.Column(scale=3):

            video_input = gr.Video(
                label="📹 Upload Video"
            )

            video_output = gr.Video(
                label="🎯 AI Processed Video"
            )

            report_output = gr.Markdown(
                label="📊 Detection Report"
            )

    # =====================================================
    # BUTTON
    # =====================================================

    process_button = gr.Button(
        "🚀 START AI DETECTION & TRACKING",
        variant="primary",
        size="lg"
    )

    process_button.click(
        fn=process_video,
        inputs=[
            video_input,
            confidence
        ],
        outputs=[
            video_output,
            report_output
        ]
    )

    gr.Markdown(
        """
        ---
        ## 🧠 Technology Stack

        **Python • YOLO11 • YOLO Pose • ByteTrack • OpenCV • Gradio**

        Built as a computer vision portfolio project.
        """
    )


# =========================================================
# START GRADIO
# =========================================================

demo.launch(
    share=True
      )
