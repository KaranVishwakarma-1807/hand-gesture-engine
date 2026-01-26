# Hand Gesture Engine

A modular, extensible hand gesture recognition engine built in Python using MediaPipe landmarks.
Designed for real-time applications, clean architecture, and easy integration into games, apps, and AI projects.

It is designed to be:
- beginner-friendly
- fast & real-time
- easy to integrate
- backend-agnostic (CPU / GPU ready)
- production-ready (configurable, logged, packaged)

Perfect for:
- Computer Vision projects
- Gesture-controlled apps
- Games & UI interaction
- Research & prototyping

## Features

- Modular gesture detection system
- Real-time hand landmark processing
- Centralized gesture recognizer (brain logic)
- Configurable thresholds (pinch, thumb, etc.)
- Built-in logging (debug & production ready)
- CPU / GPU backend auto-selection
- Clean project structure
- Confidence scoring
- Stable public API
- Ready for extension with custom gestures

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
├── setup.py</br>
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
Now, you can also directly install the module, if you just want to
- use the pre-built engine for your project
- try it out

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

## GestureEngine - BackEnd

```
engine = GestureEngine(
    backend="AUTO",  # AUTO | CPU | GPU
    config=config
)
```
Backends:
- AUTO - selects best available backend
- CPU - forced CPU execution
- GPU - uses GPU if supported

## Output Format

```bash
frame, gesture = engine.process(frame)
```

If a gesture is detected:
```bash
gesture = ("THUMBS_UP", 0.92)
```

If not:
```bash
gesture = None
```

## Logging

Enable logging via config:
```
GestureConfig(enable_logging=True)
```

Logs include:
- Backend selection
- Detection failures
- Gesture recognition results

## Extending with Custom Gestures

Add a new gesture in ```gestures.py```:
```
def is_custom(hand, config):
    # CUSTOM GESTURE LOGIC
    return some_condition
```

Register it in ```recognizer.py```:
```
if is_custom(hand, config):
    return "CUSTOM", 0.9
```

- (Optional) Add config parameters

## Requirements

- Python >= 3.9
- OpenCV
- NumPy
- MediaPipe</br>
(Installed automatically via pip)

## Versioning

Current version: v0.1.1</br>
Follows semantic versioning</br>
API stability guaranteed for v0.x</br>

### Future Ideas

Roadmap

- Gesture smoothing
- Multi-hand support
- Custom gesture training
- Mobile optimization
- ONNX / TensorRT backend

## Credit

https://tree.nathanfriend.com/</br>
Here, you can make you custom project directory trees for the markdown file.</br>
Definietly, check it out, if you want the same.</br>
Very useful!

**Also:**</br>
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

## Contributing

Pull requests are welcome.</br>
Open an issue for major changes.</br>
Steps:
```
git clone https://github.com/KaranVishwakarma-1807/hand-gesture-engine
cd hand-gesture-engine
pip install -e .
```

## Final Note

If this project helps you:
- Star it on GitHub
- Share it on PyPI
- Build cool gesture-powered apps!

### To know more about the package visit:
https://pypi.org/project/hand-gesture-engine/0.1.1/
