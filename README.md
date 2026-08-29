🤖 AI Video Monitoring, Object Tracking & Analysis System

An AI-powered computer vision system built with YOLO11, YOLO11 Pose, ByteTrack, OpenCV, and Gradio to detect, track, count, and analyze objects in video footage.



🎯 What Does This Project Do?

The system analyzes uploaded video footage and provides information about people and objects.


It can:



👥 Detect people

🚶 Detect moving people

🪑 Estimate sitting people

🧍 Estimate standing people

🚗 Detect vehicles

🪑 Detect chairs

🆔 Assign tracking IDs

🔢 Count detected objects

🎥 Generate an annotated video

📊 Generate a detection report



🧠 How It Works

📹 Input Video
      ↓
🤖 YOLO11 Object Detection
      ↓
🆔 ByteTrack Tracking
      ↓
🚶 Movement Analysis
      ↓
🧍 YOLO11 Pose Estimation
      ↓
🪑 Posture Analysis
      ↓
🔢 Counting & Statistics
      ↓
📊 Report + Annotated Video


🤖 YOLO11

A pre-trained YOLO11 model is used to detect objects in each video frame.


The system can detect objects such as:



Person

Car

Truck

Bus

Motorcycle

Bicycle

Chair



🆔 ByteTrack

ByteTrack tracks detected objects across consecutive frames and assigns tracking IDs.


Example:


Frame 1 → Person ID 1
Frame 2 → Person ID 1
Frame 3 → Person ID 1
Frame 4 → Person ID 1

This allows the system to follow objects as they move through the video.



🚶 Movement Analysis

The system compares a person's position between frames.


If the person's position changes beyond a defined threshold, the system considers the person to be moving.


Example:


People: 5
Moving: 3


🧍 Pose Analysis

The project uses YOLO11 Pose to detect human body keypoints.


The system analyzes:



Shoulders

Hips

Knees


These keypoints are used with a simple geometric rule to estimate whether a person is sitting.



Note: Sitting detection uses a pose-based heuristic rather than a separately trained sitting/standing classifier.




🔢 Object Counting

The system counts detected objects in the video.


Example:


👥 People: 5
🚗 Vehicles: 4
🪑 Chairs: 2

The final report also shows the maximum number of people, vehicles, and chairs detected during the video.



📊 Monitoring Dashboard

The processed video displays a monitoring dashboard containing information such as:


AI MONITORING

People: 5
Moving: 3
Sitting: 2
Standing: 3
Vehicles: 4
Chairs: 2

Bounding boxes and tracking IDs are displayed directly on the video.



🛠️ Technology Stack

Technology	Purpose
🐍 Python	Programming language
🤖 YOLO11	Object detection
🧍 YOLO11 Pose	Human pose estimation
🆔 ByteTrack	Object tracking
👁️ OpenCV	Video processing
🌐 Gradio	User interface


📁 Project Structure

ai-video-monitoring-and-object-tracking/
│
├── README.md
├── app.py
├── requirements.txt
├── yolo11n-pose.pt
└── yolo11n.pt

File	Description
app.py	Main application
requirements.txt	Required Python packages
yolo11n.pt	Pre-trained YOLO11 model
yolo11n-pose.pt	Pre-trained YOLO11 Pose model
README.md	Project documentation


🚀 How to Run

Clone the repository


git clone https://github.com/carolynendinda2-arch/ai-video-monitoring-and-object-tracking.git

Enter the project folder


cd ai-video-monitoring-and-object-tracking

Install dependencies


pip install -r requirements.txt

Start the application


python app.py

The application opens a Gradio interface where a video can be uploaded for analysis.



🆔 Challenges

One of the main challenges I encountered was tracking ID switching.


Tracking IDs can change when an object is temporarily lost because of:



Occlusion

Fast movement

Detection failure

Objects leaving and re-entering the frame


This helped me understand the difference between:


Object Detection
«What is this object?»


Object Tracking
«Is this the same object I saw before?»


Future Solution

A possible improvement is integrating Person Re-Identification (Re-ID) to improve identity consistency.



📚 What I Learned

This project gave me practical experience with:



YOLO11

YOLO11 Pose

ByteTrack

Object detection

Multi-object tracking

Object counting

Human movement analysis

Pose estimation

OpenCV

Gradio

Pre-trained AI models

Video processing


The biggest lesson was understanding how multiple computer vision components work together:


Detection → Tracking → Analysis → Counting → Visualization



🔮 Future Improvements


🧠 Dedicated human activity recognition

🔄 Person Re-Identification

📹 Real-time CCTV integration

🚪 Entry and exit monitoring

🚨 Suspicious activity detection

🔔 Automated alerts

📊 Advanced analytics dashboard

💻 Edge-device deployment



👩🏽‍💻 Author

Carolyne Njoki Ndinda


AI/ML & Computer Vision Enthusiast


Exploring:


🤖 Artificial Intelligence • 👁️ Computer Vision • 🧠 Machine Learning • 🎯 Object Detection • 🆔 Object Tracking • 🐍 Python



⭐ If you find this project interesting, consider giving the repository a star!



