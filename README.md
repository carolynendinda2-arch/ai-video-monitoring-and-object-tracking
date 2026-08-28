🤖 AI Video Monitoring & Object Tracking System
An AI-powered video monitoring system built with YOLO and ByteTrack for detecting and tracking objects in video footage.
The system processes video frames in real time, detects objects using YOLO, and assigns tracking IDs using ByteTrack so objects can be followed across consecutive frames.
🚀 Project Overview
Traditional video monitoring requires a person to continuously watch cameras and identify what is happening.
This project explores how computer vision can assist with that process by automatically:
👁️ Detecting objects in video
🆔 Assigning unique tracking IDs
🎥 Tracking objects across frames
📊 Monitoring multiple objects simultaneously
⚡ Processing video using computer vision
🧠 How It Works
Input Video
     ↓
YOLO Object Detection
     ↓
Detected Objects
     ↓
ByteTrack
     ↓
Tracking IDs
     ↓
AI Video Monitoring
YOLO
YOLO is responsible for detecting objects in each video frame.
ByteTrack
ByteTrack takes the detections from YOLO and associates objects across frames, allowing the system to maintain tracking IDs.
For example:
Frame 1 → Person ID 1
Frame 2 → Person ID 1
Frame 3 → Person ID 1
Frame 4 → Person ID 1
🛠️ Technologies
Python
YOLO
Ultralytics
ByteTrack
OpenCV
PyTorch
Computer Vision
🎥 Video Monitoring
The system can analyze video footage and display bounding boxes around detected objects together with their tracking IDs.
Example:
Person → ID 1
Person → ID 2
Truck  → ID 3
This makes it possible to monitor multiple objects within the same video.
🆔 Tracking Challenges
One of the challenges encountered during development was tracking ID switching.
When an object is temporarily lost because of occlusion, fast movement, or detection failure, the tracker may assign a new ID when the object is detected again.
This project helped me understand the difference between:
Object Detection
What is this object?
and
Object Tracking
Is this the same object I saw in the previous frame?
🔮 Future Improvements
Future versions of the system could include:
Person Re-Identification (Re-ID)
More reliable identity tracking
Real-time CCTV camera integration
Object counting
Entry and exit monitoring
Suspicious activity detection
Automated alerts
Web-based monitoring dashboard
Edge-device deployment
📚 What I Learned
Through this project, I gained practical experience with:
YOLO object detection
Multi-object tracking
ByteTrack
OpenCV video processing
Video inference
Tracking IDs
Debugging real-world computer vision problems
Building AI monitoring systems
The project also showed me that building a computer vision system is not only about training a model — detection, tracking, video processing, and deployment all have to work together.
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
