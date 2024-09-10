import cv2
import numpy as np

# Known diameter of the coin (e.g., in millimeters)
KNOWN_DIAMETER = 0.9551  # Diameter of a US quarter in millimeters


def calculate_pixel_to_real_ratio(known_diameter, pixel_diameter):
    return known_diameter / pixel_diameter


def calculate_depth(pixel_to_real_ratio, pixel_diameter):
    print("pr",pixel_to_real_ratio,"PD",pixel_diameter)
    real_diameter =  25.4* pixel_to_real_ratio
    depth = real_diameter - KNOWN_DIAMETER
    print("kd",KNOWN_DIAMETER)
    print("rd",real_diameter,"dep",depth)
    return depth


def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to open image file {image_path}")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve circle detection
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Apply the Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=50, param2=30, minRadius=10, maxRadius=50)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        coin_detected = False
        for (x, y, r) in circles:
            # Assuming the coin has the largest radius among detected circles
            if r > 10:  # Adjust the threshold value as needed
                coin_detected = True
                pixel_diameter = r * 2
                cv2.circle(image, (x, y), r, (0, 255, 0), 2)
                cv2.putText(image, f"Coin", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                break

        if coin_detected:
            # Calculate pixel-to-real world ratio
            pixel_to_real_ratio = calculate_pixel_to_real_ratio(KNOWN_DIAMETER, pixel_diameter)

            # Calculate depth
            depth = calculate_depth(pixel_to_real_ratio, pixel_diameter)
            cv2.putText(image, f"Tread Depth: {depth:.2f} mm", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Save the image to a file
            output_image_path = 'output_image.jpg'
            cv2.imwrite(output_image_path, image)
            print(f"Processed image saved as {output_image_path}")
        else:
            print("Error: No coin detected in the image.")
    else:
        print("Error: No circles detected in the image.")


if __name__ == "__main__":
    image_path = 'C:\\Users\\ergou\\PycharmProjects\\pythonProject\\tire_tread_depth_api\\data\\coin2.jpeg'  # Replace with the path to your image file
    process_image(image_path)
