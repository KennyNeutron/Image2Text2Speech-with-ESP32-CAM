import easyocr
import cv2


def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy.
    - Converts the image to grayscale.
    - Applies binary thresholding to enhance contrast.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text visibility
    _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # Save the preprocessed image for EasyOCR
    preprocessed_path = "preprocessed_image_easyocr.jpg"
    cv2.imwrite(preprocessed_path, threshold_image)

    return preprocessed_path


def perform_easyocr(image_path):
    """
    Perform OCR using EasyOCR.
    """
    # Initialize EasyOCR reader
    reader = easyocr.Reader(
        ["en"]
    )  # Add other languages if needed, e.g., ['en', 'fil']

    # Perform OCR
    results = reader.readtext(
        image_path, detail=0
    )  # Set detail=0 to return only the text

    return results


def main():
    # Path to the original image
    original_image_path = "captured_image.jpg"  # Replace with your image path

    # Step 1: Preprocess the image
    print("Preprocessing the image...")
    preprocessed_image_path = preprocess_image(original_image_path)

    # Step 2: Perform OCR using EasyOCR
    print("Performing OCR using EasyOCR...")
    extracted_text = perform_easyocr(preprocessed_image_path)

    # Step 3: Print the extracted text
    print("Extracted Text:")
    for line in extracted_text:
        print(line)


if __name__ == "__main__":
    main()
