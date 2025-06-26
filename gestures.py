import math

def calculate_angle(a, b, c):
    """Returns angle in degrees at point b between a and c."""
    ab = [a.x - b.x, a.y - b.y]
    cb = [c.x - b.x, c.y - b.y]
    dot = ab[0]*cb[0] + ab[1]*cb[1]
    mag_ab = math.hypot(*ab)
    mag_cb = math.hypot(*cb)
    if mag_ab * mag_cb == 0:
        return 0
    return math.degrees(math.acos(dot / (mag_ab * mag_cb)))

def get_finger_states(landmarks):
    """
    Returns list [thumb, index, middle, ring, pinky]
    Values:
      0 = down/collapsed
      1 = up/extended
      2 = thumb down (special case)
    """
    fingers = []

    # --- THUMB ---
    thumb_tip = landmarks[4]
    thumb_mcp = landmarks[2]
    thumb_angle = calculate_angle(landmarks[0], thumb_mcp, thumb_tip)

    if thumb_tip.y > thumb_mcp.y + 0.05 and thumb_angle < 140:
        fingers.append(2)  # Thumb down
    elif thumb_tip.x < landmarks[3].x and thumb_angle > 150:
        fingers.append(1)  # Thumb up
    else:
        fingers.append(0)

    # --- OTHER FINGERS ---
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]

    for tip_id, pip_id in zip(tip_ids, pip_ids):
        tip = landmarks[tip_id]
        pip = landmarks[pip_id]
        fingers.append(1 if tip.y < pip.y else 0)

    return fingers


def classify_gesture(fingers):
    """
    Map finger states to gestures:
    - [thumb, index, middle, ring, pinky]
    """
    if fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up"
    elif fingers == [2, 0, 0, 0, 0]:
        return "Thumbs Down"
    elif fingers == [0, 1, 1, 1, 1]:
        return "Open Palm"
    elif fingers == [0, 0, 0, 0, 0]:
        return "Fist"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Pointing"
    else:
        return "Unknown"
