# import cv2
# import numpy as np
#
# # Load the image of the tire
# img = cv2.imread('C:\\Users\\ergou\\PycharmProjects\\pythonProject\\tire_tread_depth_api\\data\\coin2.jpeg')
#
# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Apply thresholding to segment the tire tread from the background
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#
# # Find the contours of the tire tread
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Iterate through the contours and find the one with the maximum area
# max_contour = None
# max_area = 0
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if area > max_area:
#         max_contour = contour
#         max_area = area
#
# # Calculate the tread depth using the contour
# tread_depth = 0
# for point in max_contour:
#     x, y = point[0]
#     tread_depth += y
# tread_depth /= len(max_contour)
#
# # Draw the tire tread depth measurement on the image
# cv2.putText(img, f"Tire tread depth: {tread_depth:.2f} mm", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#
# # Save the output image to a file
# cv2.imwrite("output_image.jpg", img)
#
# print("Output image saved to output_image.jpg")
#
# # Print the tread depth
# print("Tire tread depth:", tread_depth)


import cv2
import numpy as np

# Load the image of the tire
img = cv2.imread('C:\\Users\\ergou\\PycharmProjects\\pythonProject\\tire_tread_depth_api\\data\\coin1.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the tire tread from the background
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find the contours of the tire tread
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and find the one with the maximum area
max_contour = None
max_area = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_contour = contour
        max_area = area

# Draw the contour on a new image
contour_img = np.zeros_like(img)
cv2.drawContours(contour_img, [max_contour], -1, (0, 255, 0), 2)

# Save the contour image to a file
cv2.imwrite("contour_image.jpg", contour_img)

print("Contour image saved to contour_image.jpg")