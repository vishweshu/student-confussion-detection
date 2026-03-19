# Next-Gen Confusion Detection Prototype

This is a prototype application that uses a webcam to detect whether a user is "confused" or "attentive" based on their facial expressions.

### Advanced Features
- **Decoupled Architecture**: AI interference runs asynchronously on a dedicated thread, guaranteeing 30 FPS smooth video streaming without stalling the camera.
- **Real-Time Analytics Dashboard**: A sleek, dark-mode user interface utilizing `Chart.js` to graph confusion statistics dynamically over time.

## Prerequisites

1.  **Python 3.8+**: You must have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
    *   *Important:* During Windows installation, make sure to check the box **"Add Python to PATH"**.
2.  **Webcam**: Your computer must have a working webcam connected.

## Installation Instructions

1.  **Extract the ZIP file**: Unzip the contents of this folder somewhere on your computer (e.g., your Desktop).
2.  **Open a Terminal/Command Prompt**:
    *   On Windows: Press `Win + R`, type `cmd`, and press Enter. Navigate to the extracted folder using the `cd` command (e.g., `cd Desktop\confussion_detection`).
    *   On Mac/Linux: Open the Terminal app and navigate to the extracted folder.
3.  **Install the required libraries**: Run the following command in your terminal to install all the necessary code dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: This might take a few minutes as it downloads large AI models and computer vision libraries like OpenCV and DeepFace).*

## Running the Application

1.  Once the installation is complete, make sure you are still in the terminal, inside the `confussion_detection` folder.
2.  Run the backend server with this command:
    ```bash
    python backend/app.py
    ```
3.  You should see output in the terminal saying the server is running on `http://127.0.0.1:5000` or `http://0.0.0.0:5000`.
    *(Note: The very first time you run this, it may take an extra 1-2 minutes to download DeepFace's pre-trained emotion detection weights).*
4.  Open your web browser (Chrome, Edge, Firefox, or Safari).
5.  Go to the following address:
    **http://localhost:5000**
6.  The dashboard will open, your webcam light should turn on, and you will see the live feed with the AI analyzing your emotions!

## Stopping the Application

To stop the server and turn off your webcam, go back to the terminal where the program is running and press `Ctrl + C`.
