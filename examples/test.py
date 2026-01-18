from hand_gesture import GestureEngine
from hand_gesture.config import GestureConfig
import cv2

config = GestureConfig.from_yaml("gesture_config.yaml")
engine = GestureEngine(config=config)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame, gesture = engine.process(frame)

    if gesture:
        print("Gesture:", gesture)

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1) == 27:
        break
