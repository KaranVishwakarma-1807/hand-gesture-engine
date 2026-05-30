# Hand Gesture Engine

A modular, extensible hand gesture recognition engine built in Python using MediaPipe landmarks.
Designed for real-time applications, clean architecture, and easy integration into games, apps, and AI projects.

## Features

- Modular gesture detection system
- Real-time hand landmark processing
- Centralized gesture recognizer (brain logic)
- Configurable thresholds (pinch, thumb, etc.)
- Built-in logging (debug & production ready)
- CPU / GPU backend auto-selection
- Clean project structure

## Project Structure

.</br>
├── examples/</br>
│   ├── demo.py</br>
│   ├── gesture_game.py</br>
│   └── test.py</br>
├── hand_gesture/</br>
│   ├── assests/</br>
│   │   └── hand_landmarker.task</br>
│   ├── __init__.py</br>
│   ├── config.py</br>
│   ├── engine.py</br>
│   ├── gesture.py</br>
│   ├── logging_config.py</br>
│   ├── recognizer.py</br>
│   ├── stabilizer.py</br>
│   ├── tracker.py</br>
│   └── utils.py</br>
├── .gitignore</br>
├── pyproject.toml</br>
└── README.md</br>

## Supported Gestrues

| Gesture           | Name Returned |
| ----------------- | ------------- |
| ✊ Fist            | `FIST`        |
| ✋ Open Hand       | `OPEN HAND`   |
| 👍 Thumbs Up      | `THUMBS UP`   |
| 👎 Thumbs Down    | `THUMBS DOWN` |
| ✌ Peace           | `PEACE`       |
| ☝ Pointing        | `POINTING`    |
| 👌 OK             | `OK`          |
| 🤏 Pinch          | `PINCH`       |
| 🖖 Three Fingers | `THREE`       |

## Installation

```bash
pip install mediapipe opencv-python
```

to clone the repository:

```bash
git clone https://github.com/KaranVishwakarma-1807/hand-gesture-engine.git
cd hand-gesture-engine
```

**BUT:**</br>
Now, you can also install the full module:

```bash
pip install hand-gesture-engine
```

Verify installation:

```
python -c "import hand_gesture; print(hand_gesture.__version__)"
```

## Quick Start

### Sample Code:

```
import cv2
from hand_gesture import GestureEngine, GestureConfig

config = GestureConfig()
engine = GestureEngine(backend="AUTO", config=config)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, gesture = engine.process(frame)

    if gesture:
        name, confidence = gesture
        cv2.putText(
            frame,
            f"{name} ({confidence:.2f})",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Hand Gesture Engine", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

```

## Configuration

### 1. Python Configuration

```
from hand_gesture import GestureConfig

config = GestureConfig(
    pinch_threshold=0.04,
    thumb_extension_threshold=0.6,
    finger_extension_threshold=0.5,
    min_confidence=0.7,
    enable_logging=True
)
```

### 2. YAML Confiuration (Recommended)

Add/Create ```gesture_config.yaml``` in the same working directory:
```
backend: AUTO

stability:
  hold_time: 0.35
  min_confidence: 0.6

thresholds:
  pinch: 0.04
  thumb_extended: 0.25
  finger_tolerance: 0.05
```

## Extending Gestures

To add a new gesture:

- Implement gesture logic in ```gestures.py```
- Register it in ```recognizer.py```
- (Optional) Add config parameters

### Future Ideas

Roadmap

- Gesture smoothing
- Multi-hand support
- Custom gesture training
- Mobile optimization
- ONNX / TensorRT backend

## Credit

https://choosealicense.com/</br>
This site helps you choose an open source license for your repository/project.</br>
You can get to know about the licenses and which license to choose.</br>
Very useful! 

## Author

**Karan Vishwakarma**</br>
Built with Python and Mediapipe(Google)

## License

MIT License</br>
Free to use, modify, and distribute.

## Final Note

Pull requests are welcome.</br>
Open an issue for major changes.

### To know more about the package visit:

https://pypi.org/project/hand-gesture-engine/0.1.1/