import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Variables for smooth movement
prev_x, prev_y = 0, 0
smooth_factor = 3

# Click cooldown
last_click_time = 0
click_delay = 0.5  # seconds

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Mirror view
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            # Get index finger tip position (id=8)
            index_x = int(landmarks[8].x * frame_width)
            index_y = int(landmarks[8].y * frame_height)

            # Get thumb tip position (id=4)
            thumb_x = int(landmarks[4].x * frame_width)
            thumb_y = int(landmarks[4].y * frame_height)

            # Convert coordinates to screen space
            screen_x = int(screen_width / frame_width * index_x)
            screen_y = int(screen_height / frame_height * index_y)

            # Smooth the movement
            curr_x = prev_x + (screen_x - prev_x) / smooth_factor
            curr_y = prev_y + (screen_y - prev_y) / smooth_factor
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Draw markers
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 255), -1)

            # Detect pinch for click
            distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5
            if distance < 40:  # Pinch threshold
                current_time = time.time()
                if current_time - last_click_time > click_delay:
                    pyautogui.click()
                    last_click_time = current_time

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
