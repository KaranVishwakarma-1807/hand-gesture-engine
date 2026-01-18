import cv2
from hand_gesture.engine import GestureEngine
from hand_gesture.config import GestureConfig

config = GestureConfig(
    thumb_distance_threshold=0.22,
    pinch_threshold=0.045,
    hold_time=0.4
)

engine = GestureEngine(backend="AUTO", config=config)

cap = cv2.VideoCapture(0)
WINDOW_NAME = "Gesture Engine"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame, gesture = engine.process(frame)


    if gesture:
        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    if cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        break
    

cap.release()
cv2.destroyAllWindows()
