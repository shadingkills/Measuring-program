import cv2
import numpy as np

def measure_length(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(param) < 4:
        param.append((x, y))
        if len(param) == 2:
            cv2.line(image_copy, param[0], param[1], (0, 255, 0), 2)
            cv2.imshow('Image', image_copy)
        elif len(param) == 4:
            cv2.line(image_copy, param[2], param[3], (255, 0, 0), 2)
            cv2.imshow('Image', image_copy)

# Load the image
image = cv2.imread('tool.jpg')
image_copy = image.copy()

# Create a window to display the image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', image)

# Initialize the parameter list for storing measurement points and reference length
param = []
reference_length = None
reference_pixel_length = None  # Initialize reference_pixel_length

# Register the callback function to the image window
cv2.setMouseCallback('Image', measure_length, param)

# Prompt the user to enter the reference length
print("Enter the reference length in centimeters:")

# Wait until 'q' is pressed or the reference length is entered
while True:
    # Check for the key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed or the reference length is entered, exit the loop
    if key == ord('q') or reference_length is not None:
        break

# If the reference length is entered, store it
if reference_length is None:
    reference_length = float(input("Reference Length: "))

# Prompt the user to click on two points for the first line
print("Click on two points to measure the length of the first line.")

# Wait until two points have been clicked or 'q' is pressed
while True:
    # Display the image
    cv2.imshow('Image', image_copy)

    # Check for the key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed or two points have been clicked, exit the loop
    if key == ord('q') or len(param) == 2:
        break

# If two points have been clicked for the first line, calculate the reference length
if len(param) == 2:
    reference_points = param.copy()
    reference_pixel_length = np.sqrt((reference_points[1][0] - reference_points[0][0]) ** 2 + (reference_points[1][1] - reference_points[0][1]) ** 2)
    print("Reference Length:", reference_length, "cm")

# Prompt the user to click on two points for the second line
print("Click on two points to measure the length of the second line.")

# Wait until two points have been clicked or 'q' is pressed
while True:
    # Display the image
    cv2.imshow('Image', image_copy)

    # Check for the key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed or two points have been clicked, exit the loop
    if key == ord('q') or len(param) == 4:
        break

# If two points have been clicked for the second line, calculate its length
if len(param) == 4:
    second_line_points = param[2:]
    second_pixel_length = np.sqrt((second_line_points[1][0] - second_line_points[0][0]) ** 2 + (second_line_points[1][1] - second_line_points[0][1]) ** 2)
    measured_length = (second_pixel_length / reference_pixel_length) * reference_length
    print("Measured length of the second line:", measured_length, "cm")

# Keep displaying the image until 'q' is pressed for the third time
quit_counter = 0
while True:
    # Display the image
    cv2.imshow('Image', image_copy)

    # Check for the key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed, increment the quit_counter
    if key == ord('q'):
        quit_counter += 1

    # If 'q' has been pressed for the third time, exit the loop
    if quit_counter >= 3:
        break

# Close the image window
cv2.destroyAllWindows()