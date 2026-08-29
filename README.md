🤖 AI Video Monitoring, Object Tracking & Analysis System
An AI-powered computer vision system built with YOLO11, YOLO11 Pose, ByteTrack, OpenCV, and Gradio for detecting, tracking, counting, and analyzing people and objects in video footage.
The system processes uploaded videos frame by frame, detects objects, assigns tracking IDs, analyzes human movement and posture, and generates a detection report.
🎯 Project Overview
This project explores how Artificial Intelligence and Computer Vision can be used to automate video monitoring and extract useful information from video footage.
The system can:
👥 Detect people
🚶 Identify moving people based on tracked movement
🪑 Analyze human posture to estimate sitting
🧍 Estimate standing people
🚗 Detect and count vehicles
🪑 Detect and count chairs
🆔 Assign tracking IDs using ByteTrack
🎥 Track objects across consecutive frames
📊 Generate a detection report
🎬 Produce an annotated output video
🧠 How It Works
Input Video
     ↓
YOLO11 Object Detection
     ↓
Object Detection + ByteTrack
     ↓
Tracking IDs & Movement Analysis
     ↓
YOLO11 Pose Estimation
     ↓
Posture Analysis
     ↓
Counting & Statistics
     ↓
Annotated Video + Detection Report
🤖 YOLO11 Object Detection
The project uses a pre-trained YOLO11 model to detect objects in each video frame.
The system identifies objects such as:
Person
Car
Truck
Bus
Motorcycle
Bicycle
Chair
The detected objects are then passed to the tracking system.
🆔 ByteTrack Object Tracking
ByteTrack is used to associate detected objects across consecutive frames.
Each tracked object can receive a unique tracking ID.
For example:
Frame 1 → Person ID 1
Frame 2 → Person ID 1
Frame 3 → Person ID 1
Frame 4 → Person ID 1
This allows the system to follow objects as they move through the video.
🚶 Movement Analysis
The system keeps track of the previous position of each detected person.
When the person's position changes by more than a defined distance threshold, the system considers the person to be moving.
This allows the dashboard to display information such as:
People: 5
Moving: 3
🧍 Pose & Posture Analysis
The project also uses YOLO11 Pose to detect human body keypoints.
The system uses body keypoints including:
Shoulders
Hips
Knees
A simple geometric heuristic is then applied to estimate whether a detected person is sitting.
The dashboard can therefore display:
Sitting: 2
Standing: 3
Note: Sitting detection is based on a pose-based heuristic rather than a separately trained sitting/standing classification model.
🔢 Object Counting
The system counts detected objects within each video frame and keeps track of maximum observed counts.
The monitoring dashboard can provide information such as:
People: 5
Vehicles: 4
Chairs: 2
The final detection report also provides maximum detected people, vehicles, chairs, and the total number of processed frames.
📊 AI Monitoring Dashboard
The processed video contains an on-screen monitoring dashboard displaying:
AI MONITORING

People: 5
Moving: 3
Sitting: 2
Standing: 3
Vehicles: 4
Chairs: 2
Bounding boxes and tracking IDs are also displayed on detected objects.
🛠️ Technology Stack
🐍 Python
🤖 Ultralytics YOLO11
🧍 YOLO11 Pose
🆔 ByteTrack
👁️ OpenCV
🌐 Gradio
📦 Pre-trained YOLO models
📁 Project Structure
ai-video-monitoring-and-object-tracking/
│
├── README.md
├── app.py
├── requirements.txt
├── yolo11n-pose.pt
└── yolo11n.pt
📄 File Description
File
Purpose
app.py
Main application containing detection, tracking, pose analysis, counting, and Gradio interface
requirements.txt
Python dependencies required by the project
yolo11n.pt
Pre-trained YOLO11 object detection model
yolo11n-pose.pt
Pre-trained YOLO11 pose estimation model
README.md
Project documentation
🚀 Getting Started
1. Clone the repository
git clone https://github.com/carolynendinda2-arch/ai-video-monitoring-and-object-tracking.git
2. Navigate into the project
cd ai-video-monitoring-and-object-tracking
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
The application launches a Gradio interface where a video can be uploaded for processing.
🆔 Tracking Challenges
One of the main challenges encountered during development was tracking ID switching.
An object's tracking ID may change when the object is temporarily lost because of:
Occlusion
Fast movement
Detection failure
Objects leaving and re-entering the frame
This project helped me understand the difference between:
Object Detection
"What is this object?"
Object Tracking
"Is this the same object I saw in the previous frame?"
A future improvement would be integrating Person Re-Identification (Re-ID) to improve identity consistency when a person temporarily disappears from the camera view.
📚 What I Learned
Through this project, I gained practical experience with:
YOLO11 object detection
YOLO11 Pose estimation
ByteTrack multi-object tracking
Object counting
Human movement analysis
Pose-based posture analysis
OpenCV video processing
Gradio interfaces
Pre-trained AI models
Video inference
Tracking IDs
Debugging real-world computer vision problems
Most importantly, this project taught me how different computer vision components can work together to transform raw video into useful information.
YOLO detects the objects, ByteTrack follows them, YOLO Pose analyzes human posture, and OpenCV + Gradio turn the results into a usable monitoring application.
🔮 Future Improvements
Future versions could include:
🧠 A dedicated human activity classification model
🔄 Person Re-Identification (Re-ID)
📹 Real-time CCTV camera integration
🚪 Entry and exit monitoring
🚨 Suspicious activity detection
🔔 Automated alerts
📊 Advanced analytics dashboard
💻 Edge-device deployment
🎯 Improved sitting/standing classification
👩🏽‍💻 Author
Carolyne Njoki Ndinda
AI/ML & Computer Vision Enthusiast
Currently exploring:
🤖 Artificial Intelligence
👁️ Computer Vision
🧠 Machine Learning
🎯 Object Detection
🆔 Object Tracking
🐍 Python
⭐ If you find this project interesting, consider giving the repository a star!
