import requests
from PIL import Image
from io import BytesIO
import pytesseract
import pyttsx3

# Replace with your ESP32-CAM IP address
ESP32_CAM_IP = "http://192.168.27.10"

def capture_image():
    """Capture an image from the ESP32-CAM."""
    try:
        response = requests.get(f"{ESP32_CAM_IP}/capture")
        if response.status_code == 200:
            # Display the captured image
            image = Image.open(BytesIO(response.content))
            image.show()

            # Save the image locally
            image_path = "captured_image.jpg"
            image.save(image_path)
            print(f"Image saved as '{image_path}'")
            return image_path
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while capturing the image: {e}")
        return None

def perform_ocr(image_path):
    """Extract text from the captured image using OCR."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print("Extracted Text:", text)
        return text
    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return ""

def text_to_speech(text):
    """Convert extracted text to speech."""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")

def main():
    """Main workflow."""
    # Step 1: Capture image from ESP32-CAM
    image_path = capture_image()
    if not image_path:
        print("Failed to capture image. Exiting...")
        return

    # Step 2: Perform OCR on the captured image
    text = perform_ocr(image_path)
    if not text.strip():
        print("No text found in the image. Exiting...")
        return

    # Step 3: Convert extracted text to speech
    text_to_speech(text)

if __name__ == "__main__":
    main()
