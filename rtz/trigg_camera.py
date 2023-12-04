import cv2
from pyzbar.pyzbar import decode


# Function to capture a photo from the camera and return the image
def capture_photo():
    # Initialize the camera (0 is typically the built-in camera, but you can change this if needed)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return None

    # Capture a single frame (photo)
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    if ret:
        return frame
    else:
        print("Error: Could not capture a photo.")
        return None


# Function to read QR code from an image and return the decoded string
def read_qr_code(image):
    # Decode QR code
    decoded_objects = decode(image)

    if decoded_objects:
        # Extract and return the first decoded object (assuming there's only one QR code)
        return decoded_objects[0].data.decode("utf-8")
    else:
        return "No QR code found in the image."


# Capture a photo from the camera
photo = capture_photo()

if photo is not None:
    # Call the function to read the QR code from the captured photo
    result = read_qr_code(photo)

    # Print the result
    print("QR Code Content:", result)
