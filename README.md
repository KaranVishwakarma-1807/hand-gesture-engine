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

.                                     # ROOT DIRECTORY
├── examples/
│   ├── demo.py
│   ├── gesture_game.py
│   └── test.py
├── hand_gesture/
│   ├── assests/
│   │   └── hand_landmarker.task      # HAND LANDMARK MODEL
│   ├── __init__.py
│   ├── config.py                     # Gesture configuration
│   ├── engine.py                     # Main gesture engine
│   ├── gesture.py                    # Individual gesture logic
│   ├── logging_config.py             # Logging setup
│   ├── recognizer.py                 # Gesture recognisation logic
│   ├── stabilizer.py                 # Gesture stabilizer login
│   ├── tracker.py                    # Gesture tracker
│   └── utils.py                      # Additional functionalities
├── .gitignore
├── pyproject.toml
└── README.md

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
cd gesture-engine
```

## Basic Usage

```
from gesture_engine.engine import GestureEngine
from gesture_engine.config import GestureConfig

engine = GestureEngine(
    backend="AUTO",
    config=GestureConfig()
)

gesture, confidence = engine.process(hand_landmarks)

print(gesture, confidence)
```

## Extending Gestures

To add a new gesture:

- Implement gesture logic in ```gestures.py```
- Register it in ```recognizer.py```
- (Optional) Add config parameters

## Future Ideas

Roadmap

- Gesture smoothing
- Multi-hand support
- Custom gesture training
- Mobile optimization
- ONNX / TensorRT backend

## License

MIT License
Free to use, modify, and distribute.

## Author

Karan Vishwakarma
Built with Python and Mediapipe(Google)

## Credit

```https://tree.nathanfriend.com/```
Here, you can make you custom project directory trees for the markdown file.
Definietly, check it out, if you want the same.
Very useful!

## Quick Start

```
import cv2
from hand_gesture import GestureEngine, GestureConfig

config = GestureConfig.from_yaml("gesture_config.yaml")
engine = GestureEngine(config=config)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame, gesture = engine.process(frame)

    if gesture:
        print("Detected:", gesture)

    cv2.imshow("Gesture Engine", frame)
    if cv2.waitKey(1) == 27:
        break
```

## Configuration

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

## Contributing

Pull requests are welcome.
Open an issue for major changes.
