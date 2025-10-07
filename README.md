# Medical Report AI Assistant with Local Ollama

This project is a local web application for the interactive analysis of medical reports (images, PDFs, and text files) using multi-modal Large Language Models (LLMs) served by Ollama.

The architecture uses a Python (Flask) backend to handle file processing and communication with Ollama, and a clean HTML/JavaScript frontend for the user interface. This approach ensures all data processing remains on the user's local machine, guaranteeing privacy and security.

## How It Works

1.  **File Upload**: The user selects a report type and uploads a file (`.pdf`, `.jpg`, `.png`, `.txt`) via the web UI.
2.  **Frontend Preview**: The browser generates a quick preview of the uploaded file. For PDFs, each page is rendered as an image.
3.  **Backend Processing**: When analysis is requested, the file is sent to the Flask backend. If the file is a PDF, the server uses PyMuPDF to convert each page into a high-quality image.
4.  **Ollama Interaction**: The backend constructs a prompt, bundles it with the images or text, and sends it to the local Ollama instance for analysis.
5.  **Interactive Chat**: The generated report is displayed in a chat interface, where the user can ask follow-up questions for deeper insights.

## Features

-   **Privacy-First**: All files and analysis requests are processed locally and are never sent over the internet.
-   **Multi-modal Support**: Natively handles `.png`, `.jpg`, `.pdf`, and `.txt` files.
-   **Advanced PDF Processing**: Accurately converts multi-page PDFs into a sequence of images for comprehensive visual analysis.
-   **Interactive Chat Interface**: Allows for follow-up questions to refine and explore the initial analysis.
-   **Performance Metrics**: Displays generation time, token count, and tokens per second (TPS) for each AI response.
-   **Model Selection**: Lets the user choose different models for the initial analysis versus the follow-up chat.
-   **Clean & Responsive UI**: The interface is designed to be clear and usable on various screen sizes.

## Recommended Models

For this application to function correctly, you must use **multi-modal (vision-capable)** models from Ollama. Text-only models will fail when analyzing images or PDFs.

Here are some recommended models that work well with this tool:

-   **`puyangwang/medgemma-27b-it`**: A 27B parameter version of MedGemma fine-tuned for the medical domain. Different quantizations are available (e.g., `:q4_k_m`). This is the recommended model for high-quality, detailed analysis.
    ```bash
    ollama pull puyangwang/medgemma-27b-it
    ```
-   **`amsaravi/medgemma-4b-it`**: A smaller 4B parameter version, excellent for faster responses, especially in the follow-up chat.
    ```bash
    ollama pull amsaravi/medgemma-4b-it
    ```

## Installation

### Prerequisites

-   Python 3.8+ installed.
-   Ollama installed and running.

### Setup Procedure

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/lordpba/Medical-Report-AI-Assistant
    cd <PROJECT_FOLDER_NAME>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate the environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Ensure the Ollama service is running in the background.
2.  Start the application server from the project directory:
    ```bash
    python app.py
    ```
3.  Open your web browser and navigate to `http://127.0.0.1:5000`.

The application will now be running and ready for use.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer

AI-generated analyses may contain errors. This tool is intended for research and educational purposes only. The supervision and opinion of a qualified medical professional is always required for any clinical decisions.
