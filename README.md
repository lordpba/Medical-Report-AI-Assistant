# Medical Report AI Assistant with Local Ollama

This project is a local web application for interactive analysis of medical reports (images, PDFs, text) using Large Language Models (LLMs) via Ollama.

The architecture uses a Python (Flask) backend to handle file processing and communication with Ollama, and an HTML/JavaScript frontend for the user interface.

## Features

-   **Interactive Frontend**: A two-column interface with a report preview and a chat for follow-up questions.
-   **Multi-modal Support**: Analyzes `.png`, `.jpg`, `.pdf`, and `.txt` files.
-   **Advanced PDF Processing**: PDFs are converted into images on a page-by-page basis for accurate visual analysis by multi-modal models.
-   **Model Selection**: Allows choosing different models for the initial analysis and for the chat.
-   **Robust Backend**: All complex logic is handled by a Python server, simplifying the frontend and resolving CORS issues.

## Recommended Models

For this application to work correctly, it is essential to use **multi-modal (visual)** models capable of interpreting images. Here are some recommended models available on Ollama:

-   **`puyangwang/medgemma-27b-it:q6`**: A 27B multi-modal version of MedGemma. As of today, this specific version (`q6`) is **highly recommended** for its balance of accuracy and performance. Please note that it requires at least **24GB of GPU VRAM** to run effectively.
    ```bash
    ollama pull puyangwang/medgemma-27b-it:q6
    ```

-   **`alibayram/medgemma`**: This is a collection of MedGemma variants. When using it, make sure to select a version with visual capabilities (often indicated by the `vision` tag).
    ```bash
    # Example for a visual model from this collection (the exact tag might vary)
    ollama pull alibayram/medgemma
    ```

**Important**: Text-only models will not be able to analyze images or PDF files. Always check that the model you are using has multi-modal capabilities.

## Installation

### Prerequisites

-   Python 3.8+ installed.
-   Ollama installed and running. (Make sure you have pulled the models you intend to use, e.g., `ollama pull puyangwang/medgemma-27b-it`).

### Setup Procedure

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <FOLDER_NAME>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Make sure the Ollama service is running.
2.  Start the application server:
    ```bash
    python app.py
    ```
3.  Open your browser and navigate to `http://127.0.0.1:5000`.

The application will now be running and ready to use.

---

## Disclaimer

**Disclaimer:** AI-generated analyses may contain errors. This tool is intended for research and educational purposes only. The supervision and opinion of a qualified medical professional is always required for any clinical decisions.
