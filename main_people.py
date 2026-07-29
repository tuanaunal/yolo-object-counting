"""
insan saga mi sola mi gittigini sayma yolo kullanarak

data: https://www.kaggle.com/datasets/khitthanhnguynphan/crowduit
"""

import cv2  # opencv
import numpy as np
from ultralytics import YOLO

# model yukleme
model = YOLO("yolov8n.pt")  # yolonun v8 nano modeli

# video dosyasinin acilmasi
cap = cv2.VideoCapture("2.mp4")

# 1 frame oku ve video calisiyor mu diye bak
success, frame = cap.read()
if not success:
    exit("video calismiyor")

# yeniden boyutlandirma
frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)
frame_height, frame_width = frame.shape[:2]

# ortaya dikey cizgi, bu cizgiyi geceleri count edelim
line_x = int(frame_width * 0.5)
offset = 10

# sayaclar
giren = 0
cikan = 0
counted_ids = set()
person_last_x = {}

# yolo ile insan sayma
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)

    cv2.line(frame, (line_x, 0), (line_x, frame_height), (0, 0, 255), 2)

    cv2.imshow("avm yon takibi", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()