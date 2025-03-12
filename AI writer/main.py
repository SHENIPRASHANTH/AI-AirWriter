import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

prev_x, prev_y = None, None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            h, w, _ = frame.shape

            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            x_thumb, y_thumb = int(thumb_tip.x * w), int(thumb_tip.y * h)

            distance = math.hypot(x - x_thumb, y - y_thumb)

            if distance < 40:  
                if prev_x is not None and prev_y is not None:
                    cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 255, 255), 5)
                prev_x, prev_y = x, y
            else:
                prev_x, prev_y = None, None  

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    cv2.imshow("Finger Writing (Lift to Stop)", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):  # Clear screen when 'c' is pressed
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    elif key == ord('q'):  # Quit when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()
