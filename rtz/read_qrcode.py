import cv2
from pyzbar.pyzbar import decode


# Function to read QR code from an image and return the decoded string
def read_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Decode QR code
    decoded_objects = decode(image)

    if decoded_objects:
        # Extract and return the first decoded object (assuming there's only one QR code)
        return decoded_objects[0].data.decode("utf-8")
    else:
        return "No QR code found in the image."


# Path to the image containing the QR code
image_path = r"C:\Users\clldu\OneDrive\vsc_envir\python_lab\rtz\image.png"

# Call the function to read the QR code
result = read_qr_code(image_path)

# Print the result
print("QR Code Content:", result)
