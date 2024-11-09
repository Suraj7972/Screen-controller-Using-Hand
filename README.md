# Screen-controller-Using-Hand

Virtual Mouse and Swipe Gesture Control with Hand Tracking
This Python project utilizes hand tracking with OpenCV and MediaPipe to create a virtual mouse and swipe gesture control system for your computer.

Functionality:

Hand Tracking: Continuously detects and tracks hands using a webcam.
Virtual Mouse: Controls the mouse cursor on your screen based on the position of your thumb.
Mouse Click: Simulates a mouse click using your middle finger.
Swipe Gestures: Detects horizontal swipes with two fingers to switch between browser tabs (configurable).
How it Works:

Initialization:

Loads the MediaPipe Hands model for hand landmark detection.
Sets up the video capture from your webcam.
Defines screen resolution for accurate cursor mapping.
Hand Detection and Tracking:

Processes each video frame to detect hands.
Extracts the landmarks (key points) of the detected hands.
Virtual Mouse Control:

Identifies the tip of the thumb landmark.
Maps the thumb position on the frame to the corresponding screen coordinates using linear interpolation.
Moves the mouse cursor to the calculated screen coordinates.
Mouse Click:

Monitors the middle finger landmark.
Triggers a simulated mouse click when the middle finger bends further than the index finger (configurable).
Swipe Gestures (Optional):

Tracks the movement of the thumb over multiple frames.
Detects horizontal swipes based on the movement distance.
Simulates keyboard shortcuts (e.g., Ctrl + Tab) for switching browser tabs based on swipe direction (configurable).
Requirements:

Python 3.x
OpenCV library (pip install opencv-python)
MediaPipe library (pip install mediapipe)
PyAutoGUI library (pip install pyautogui)
Running the Script:

Save the code as a Python script (e.g., virtual_mouse.py).

Install required libraries:

Bash
pip install opencv-python mediapipe pyautogui
Use code with caution.

Run the script:

Bash
python virtual_mouse.py
Use code with caution.

Press the 'q' key to exit the program.

Customization:

You can modify the script to:
Change the keyboard shortcuts used for swipe gestures.
Adjust the sensitivity of the mouse control and click detection.
Implement additional gestures for different functionalities.
