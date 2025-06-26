# Gesture-Controlled Media Player

A Python application that uses your webcam and hand gestures to control media playback (play/pause, next track, volume up/down, etc.) using OpenCV, MediaPipe, and pyautogui.

## Features
- Real-time hand gesture recognition
- Control media player actions with gestures:
  - **Open Palm**: Play/Pause
  - **Fist**: Pause
  - **Thumbs Up**: Volume Up
  - **Thumbs Down**: Volume Down
  - **Pointing**: Next Track
- Visual feedback overlay
- Gesture smoothing for accuracy

## Setup
1. Install Python 3.7+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Ensure your webcam is connected.
- Run the script. A window will open showing the webcam feed and detected gesture.
- Use the gestures above to control your media player.
- Press `q` to quit.

## Troubleshooting
- If the webcam does not open, try changing the camera index in `main.py` (`cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`).
- Some media actions may not work on all platforms or media players. You may need to adjust the key mappings in the code.
- If you get missing module errors, ensure all dependencies are installed.

## Extending
- To add new gestures, edit `gestures.py` and update the mapping in `main.py`.
- For test/debug mode, set `TEST_MODE = True` in `main.py` (if enabled).

---

**Developed as a gesture recognition project using computer vision.** 