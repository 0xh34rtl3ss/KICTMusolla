#!/bin/bash

# Run the YOLOv5 object detection program
nohup python3 ./yolov5/detect.py --classes 0 --source ./yolov5/115534_final2.mp4 --weights ./yolov5/rb_yolov5m_v2.pt --view-img &

# Run the Flask web application
nohup python3 app.py &




