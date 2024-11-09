import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2)

Draw = mp.solutions.drawing_utils

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

# Initialize pointer coordinates
pointer_x = 0
pointer_y = 0

# Initialize screen size for mapping pointer coordinates
screen_width, screen_height = pyautogui.size()

# Initialize swipe gesture variables
prev_x = 0
prev_y = 0

while True:
    # Read video frame by frame
    _, frame = cap.read()

    # Flip image
    frame = cv2.flip(frame, 1)

    # Convert BGR image to RGB image
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    Process = hands.process(frameRGB)

    landmarkList = []
    # if hands are present in image(frame)
    if Process.multi_hand_landmarks:
        # detect handmarks
        for handlm in Process.multi_hand_landmarks:
            for _id, landmarks in enumerate(handlm.landmark):
                # store height and width of image
                height, width, color_channels = frame.shape

                # calculate and append x, y coordinates
                # of handmarks from image(frame) to lmListqq
                x, y = int(landmarks.x * width), int(landmarks.y * height)
                landmarkList.append([_id, x, y])

            # draw Landmarks
            Draw.draw_landmarks(frame, handlm, mpHands.HAND_CONNECTIONS)

    # If landmarks list is not empty
    if landmarkList != []:
        # store x,y coordinates of (tip of) thumb
        x_1, y_1 = landmarkList[4][1], landmarkList[4][2]

        # store x,y coordinates of (tip of) index finger
        x_2, y_2 = landmarkList[8][1], landmarkList[8][2]

        # draw circle on thumb and index finger tip
        cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED)
        cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)

        # draw line from tip of thumb to tip of index finger
        cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)

        # Update pointer coordinates based on thumb positionq
        pointer_x = int(np.interp(x_1, [0, width], [0, screen_width]))
        pointer_y = int(np.interp(y_1, [0, height], [0, screen_height]))

        # Control screen click with middle finger
        if landmarkList[12][2] < landmarkList[10][2]:
            # Simulate mouse click at pointer coordinates
            pyautogui.click(x=pointer_x, y=pointer_y)

        # Detect swipe gesture
        if prev_x != 0 and prev_y != 0:
            # Calculate the movement distance
            dx = x_1 - prev_x
            dy = y_1 - prev_y

            # Determine the swipe direction based on the movement distance
            if abs(dx) > abs(dy):
                if dx > 0:
                    pyautogui.hotkey('ctrl', 'tab')  # Switch to next tab
                else:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')  # Switch to previous tab

        # Store the current coordinates for the next frame
        prev_x = x_1
        prev_y = y_1

    # Draw the pointer
    cv2.circle(frame, (pointer_x, pointer_y), 10, (255, 0, 0), cv2.FILLED)

    # Display Video and when 'q' is entered, destroy the window
    cv2.imshow('Image', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the VideoCapture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
