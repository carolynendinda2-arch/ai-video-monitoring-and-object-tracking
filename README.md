🤖 AI Video Monitoring & Object Tracking System
An AI-powered computer vision system that detects and tracks objects in video footage using Ultralytics YOLO and ByteTrack.
The system processes video frames, detects objects, and assigns tracking IDs so that objects can be followed across consecutive frames.
🎯 Project Overview
Traditional video monitoring requires a person to continuously watch camera footage and identify what is happening.
This project explores how Artificial Intelligence and Computer Vision can assist with video monitoring by automatically:
👁️ Detecting objects in video
🆔 Assigning tracking IDs
🎥 Tracking objects across consecutive frames
📊 Monitoring multiple objects simultaneously
⚡ Processing video using computer vision
🧠 How It Works
Input Video
     ↓
Ultralytics YOLO
     ↓
Object Detection
     ↓
ByteTrack
     ↓
Tracking IDs
     ↓
AI Video Monitoring
🤖 Ultralytics YOLO
Ultralytics YOLO is responsible for detecting objects in each video frame.
For this project, I used a pre-trained YOLO model to detect objects in the video.
🆔 ByteTrack
ByteTrack is used to track detected objects across consecutive video frames.
It associates detections between frames and assigns tracking IDs.
For example:
Frame 1 → Person ID 1
Frame 2 → Person ID 1
Frame 3 → Person ID 1
Frame 4 → Person ID 1
This allows the system to follow objects as they move through the video.
🛠️ Technologies Used
🐍 Python
🤖 Ultralytics YOLO
🆔 ByteTrack
📦 Pre-trained YOLO Model
👁️ OpenCV
🎥 Video Monitoring
The system analyzes video footage and displays bounding boxes around detected objects together with their tracking IDs.
Example:
Person → ID 1
Person → ID 2
Truck  → ID 3
This makes it possible to monitor multiple objects within the same video.
🆔 Tracking Challenges
One of the main challenges encountered during development was tracking ID switching.
An object's tracking ID can change when the object is temporarily lost because of:
Occlusion
Fast movement
Detection failure
Objects leaving and re-entering the frame
This project helped me understand the important difference between:
Object Detection
"What is this object?"
Object Tracking
"Is this the same object I saw in the previous frame?"
One possible improvement is integrating Person Re-Identification (Re-ID) to make identity tracking more reliable when objects temporarily disappear from the camera view.
📁 Project Structure
AI_VIDIO_MONITORING_AND_OBJECT_TRACKING_SYSTEM/
│
├── README.md
├── app.py
├── requirements.txt
├── yolo11n-pose.pt
└── yolo11n.pt
🚀 Getting Started
1. Clone the repository
git clone https://github.com/carolynendinda2-arch/AI_VIDIO_MONITORING_AND_OBJECT_TRACKING_SYSTEM.git
2. Navigate into the project
cd AI_VIDIO_MONITORING_AND_OBJECT_TRACKING_SYSTEM
3. Install the required dependencies
pip install -r requirements.txt
4. Run the application
python app.py
Note: Make sure Python and the required dependencies are installed before running the application.
🔮 Future Improvements
Future versions of the system could include:
🧍 Person Re-Identification (Re-ID)
📹 Real-time CCTV camera integration
🔢 Automatic object counting
🚪 Entry and exit monitoring
🚨 Suspicious activity detection
🔔 Automated alerts
📊 Web-based monitoring dashboard
💻 Edge-device deployment
📚 What I Learned
Through this project, I gained practical experience with:
Ultralytics YOLO
Object detection
ByteTrack
Multi-object tracking
OpenCV video processing
Video inference
Tracking IDs
Debugging real-world computer vision problems
Working with pre-trained models
Building AI video monitoring systems
Most importantly, this project taught me that building a computer vision system is not only about using a model.
Detection, tracking, video processing, debugging, and understanding how different components work together are all important when building a practical AI system.
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
