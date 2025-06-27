import cv2
import mediapipe as mp
from gestures import get_finger_states, classify_gesture
from collections import deque
import pyautogui
import time

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Gesture history buffer for smoothing
gesture_history = deque(maxlen=5)

# Gesture color mapping for feedback
gesture_colors = {
    "Open Palm": (0, 255, 0),
    "Fist": (0, 0, 255),
    "Thumbs Up": (255, 255, 0),
    "Thumbs Down": (255, 0, 0),
    "Pointing": (255, 0, 255),
    "Mute": (0, 100, 255),
    "Shuffle": (128, 0, 255),
    "Unknown": (200, 200, 200),
    "No Hand Detected": (100, 100, 100)
}

# Action cooldown (in seconds)
last_action_time = 0
action_delay = 1.0  # 1 second

TEST_MODE = False  # Set to True to disable actual key presses for debugging

def perform_action(gesture, test_mode=False):
    action_map = {
        "Open Palm": ("space", "Play/Pause"),
        "Fist": ("space", "Pause"),
        "Thumbs Up": ("volumeup", "Volume Up"),
        "Thumbs Down": ("volumedown", "Volume Down"),
        "Pointing": ("nexttrack", "Next Track"),
        "Mute": ("volumemute", "Mute"),
        "Shuffle": (["ctrl", "s"], "Shuffle")
    }

    if gesture in action_map:
        key, action = action_map[gesture]

        if test_mode:
            print(f"[TEST MODE] Action: {action}")
        else:
            # Handle hotkey (like ctrl+s for shuffle)
            if isinstance(key, list):
                pyautogui.hotkey(*key)
            else:
                pyautogui.press(key)
            print(f"Action: {action}")

# Start webcam
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to read from webcam.")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        display_gesture = "No Hand Detected"
        fingers = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = get_finger_states(hand_landmarks.landmark)
                gesture = classify_gesture(fingers)

                gesture_history.append(gesture)
                display_gesture = max(set(gesture_history), key=gesture_history.count)

                # Cooldown check
                current_time = time.time()
                if current_time - last_action_time > action_delay:
                    perform_action(display_gesture, TEST_MODE)
                    last_action_time = current_time

        # Draw gesture overlay
        gesture_color = gesture_colors.get(display_gesture, (255, 255, 255))
        cv2.rectangle(frame, (5, 5), (400, 60), gesture_color, cv2.FILLED)
        cv2.putText(frame, f'Gesture: {display_gesture}', (10, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # Optional: Show finger states for debugging
        if fingers:
            cv2.putText(frame, f'States: {fingers}', (10, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow('Gesture Controlled Media Player', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
