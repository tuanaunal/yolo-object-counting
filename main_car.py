"""
Problem tanimi: video uzerinden yolo ile arac sayma
    - car
    - truck
    - otobus

YOLO ile arac tracking sonrasinde belirli bir cizgiyi gecen araclarin sayisini count edelim

data: https://www.kaggle.com/datasets/benjaminguerrieri/car-detection-videos?select=IMG_5268.MOV
"""

# import libraries
import cv2  # opencv
import numpy as np
from ultralytics import YOLO

# yardimci fonksiyon tanimlama
def get_line_side(x, y, line_start, line_end):  # objemiz line in hangi tarafinda anlamak icin kullanalim
    return np.sign((line_end[0] - line_start[0]) * (y - line_start[1]) - 
                   (line_end[1] - line_start[1]) * (x - line_start[0]))

# modeli tanimlama
model = YOLO("yolov8n.pt")

# video capture
cap = cv2.VideoCapture("IMG_5268.MOV")

success, frame = cap.read()
if not success:
    exit("Video acilamadi")

frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)
frame_height, frame_width = frame.shape[:2]

# capraz cizgi tanimlama
line_start = (int(frame_height * 0.5), frame_height)
line_end = (frame_width, int(frame_width * 0.2))

# obje tipi
counts = {"car": 0, "truck": 0, "bus": 0, "motorcycle": 0, "bicycle": 0}
counted_ids = set()
object_last_side = {}

# yolo ile arac sayimi
while True:

    success, frame = cap.read()
    if not success:
        exit("Video acilamadi")

    frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)

    # simdilik line cizme
    cv2.line(frame, line_start, line_end, (0, 0, 255), 2)

    cv2.imshow("arac takip ve sayim", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break