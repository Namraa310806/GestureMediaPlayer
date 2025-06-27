# Gesture-Controlled Media Player

A Python application that lets you control your media player using hand gestures detected via your webcam. Built with OpenCV, MediaPipe, and pyautogui, this project recognizes several intuitive hand gestures to perform actions like play/pause, next track, volume control, mute, and shuffle.

## Features
- Real-time hand gesture recognition using computer vision
- Control media playback with simple gestures
- Visual feedback overlay on webcam feed
- Gesture smoothing for improved accuracy
- Easily extendable for new gestures

## Supported Gestures
| Gesture        | Hand Pose Example         | Action         |
|---------------|--------------------------|----------------|
| Open Palm     | All fingers extended      | Play/Pause     |
| Fist          | All fingers collapsed     | Pause          |
| Thumbs Up     | Only thumb up            | Volume Up      |
| Thumbs Down   | Thumb down (special case)| Volume Down    |
| Pointing      | Only index finger up      | Next Track     |
| Mute          | Index & middle up        | Mute           |
| Shuffle       | Index & pinky up         | Shuffle        |

## Demo
<!-- Add a GIF or screenshot here if available -->

## Installation
1. **Python 3.7+ required**
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure your webcam is connected.
2. Run the application:
   ```bash
   python main.py
   ```
3. A window will open showing your webcam feed and the detected gesture.
4. Use the gestures listed above to control your media player.
5. Press `q` to quit.

## Troubleshooting
- If the webcam does not open, try changing the camera index in `main.py` (`cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`).
- Some media actions may not work on all platforms or media players. Adjust key mappings in the code if needed.
- If you get missing module errors, ensure all dependencies are installed.

## Extending the Project
- To add new gestures, edit `gestures.py` to define new finger state patterns and update the gesture-action mapping in `main.py`.
- For test/debug mode (no real key presses), set `TEST_MODE = True` in `main.py`.

---

**Developed as a gesture recognition project using computer vision.** 