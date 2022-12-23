# Run the YOLOv5 object detection program
python3 detect.py --classes 0 --source 115534_final2.mp4 --weights rb_yolov5m_v2.pt --view-img &

# Run the Flask web application
gunicorn -w 4 app:app
