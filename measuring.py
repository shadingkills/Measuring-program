import cv2
import numpy as np

image_copy = None  # Declare image_copy as a global variable

def measure_length(event, x, y, flags, param):
    global image_copy  # Access the global image_copy variable

    if event == cv2.EVENT_LBUTTONDOWN and len(param) < 4:
        param.append((x, y))
        if len(param) == 1:
            cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1)
        elif len(param) == 2:
            cv2.line(image_copy, param[0], param[1], (0, 255, 0), 2)
        elif len(param) == 3:
            cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1)
        elif len(param) == 4:
            cv2.line(image_copy, param[2], param[3], (255, 0, 0), 2)

    elif event == cv2.EVENT_MOUSEMOVE and len(param) == 1:
        if len(param) == 1:
            image_copy = image.copy()
            cv2.circle(image_copy, param[0], 5, (0, 0, 255), -1)
            cv2.line(image_copy, param[0], (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_MOUSEMOVE and len(param) == 3:
        if len(param) == 3:
            image_copy = image.copy()
            cv2.circle(image_copy, param[2], 5, (0, 0, 255), -1)
            cv2.line(image_copy, param[0], (x, y), (0, 255, 0), 2)


    cv2.imshow('Image', image_copy)


image = cv2.imread('test.jpg')
image_copy = image.copy()

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', image)

param = []
reference_length = None
reference_pixel_length = None  

# Register the callback function to the image window
cv2.setMouseCallback('Image', measure_length, param)

print("Enter the reference length in centimeters:")

# Wait until 'q' is pressed or the reference length is entered
while True:

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q') or reference_length is not None:
        break


if reference_length is None:
    reference_length = float(input("Reference Length: "))


print("Click on two points to measure the length of the first line.")


while True:

    cv2.imshow('Image', image_copy)

    key = cv2.waitKey(1) & 0xFF

  
    if key == ord('q') or len(param) == 2:
        break

# If two points have been clicked for the first line, calculate the reference length
if len(param) == 2:
    reference_points = param.copy()
    reference_pixel_length = np.sqrt((reference_points[1][0] - reference_points[0][0]) ** 2 + (reference_points[1][1] - reference_points[0][1]) ** 2)
    print("Reference Length:", reference_length, "cm")


print("Click on two points to measure the length of the second line.")

# Wait until two points have been clicked or 'q' is pressed
while True:
   
    cv2.imshow('Image', image_copy)


    key = cv2.waitKey(1) & 0xFF

  
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
   
    cv2.imshow('Image', image_copy)


    key = cv2.waitKey(1) & 0xFF

 
    if key == ord('q'):
        quit_counter += 1

  
    if quit_counter >= 3:
        break


cv2.destroyAllWindows()