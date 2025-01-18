# Image2Text2Speech with ESP32-CAM

## Project Overview

**Image2Text2Speech with ESP32-CAM** is a Python-based IoT application that uses the ESP32-CAM to capture images, extract text using Optical Character Recognition (OCR), and convert the text to speech. The application is designed for real-world deployment on Orange Pi and combines IoT, AI, and Python-based technologies for innovative text-to-speech solutions.

---

## Objectives

- Capture text from physical objects (e.g., cardboard, signs) using an ESP32-CAM.
- Extract text from the captured image using OCR.
- Convert the extracted text to speech for audio output.

---

## Tools and Technologies

### **Hardware**

- ESP32-CAM
- Orange Pi (for deployment)

### **Software**

- **Python Libraries**:
  - `pytesseract`: OCR processing
  - `pyttsx3`: Text-to-Speech synthesis
  - `Pillow`: Image processing
  - `requests`: Handling HTTP requests
- **ESP32-CAM Firmware**:
  - Arduino IDE with ESP32 libraries for hosting a web server and capturing images
- **OCR Engine**:
  - [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)

---

## Workflow

### **1. ESP32-CAM**

- Captures images and hosts them on a web server.
- The server provides access to captured images via HTTP.

### **2. Python Application**

- Fetches the captured image from the ESP32-CAM web server.
- Processes the image for OCR using Tesseract.
- Converts the extracted text into speech using a TTS library.

### **3. Deployment**

- Development is done on a Windows machine for convenience.
- Deployment is optimized for an Orange Pi running a Linux-based OS.

---

## Installation

### **1. ESP32-CAM Setup**

1. Flash the ESP32-CAM with the example sketch for hosting a web server and capturing images.
2. Configure the correct camera model and WiFi credentials in the sketch.

### **2. Python Environment**

1. Clone the repository:

   ```bash
   git clone https://github.com/KennyNeutron/Image2Text2Speech-with-ESP32-CAM.git
   cd Image2Text2Speech-with-ESP32-CAM
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Tesseract-OCR:
   ```bash
   sudo apt install tesseract-ocr  # Linux
   ```
   For Windows, download and install [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract).

---

## Usage

1. Run the Python application on your machine:
   ```bash
   python app.py
   ```
2. Ensure the ESP32-CAM is connected to the same network and capturing images.
3. Follow the instructions in the terminal to fetch images, perform OCR, and hear the text-to-speech output.

---

## Features

- IoT-based image capture using ESP32-CAM.
- OCR for text recognition from images.
- Text-to-Speech conversion for audio output.
- Lightweight deployment on Orange Pi.

---

## Future Enhancements

- Real-time image capture and processing.
- Improved OCR accuracy with advanced preprocessing techniques.
- Support for multilingual OCR and TTS.
- Enhanced UI for configuration and monitoring.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with detailed explanations of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [ESP32-CAM Arduino Library](https://github.com/espressif/arduino-esp32)
