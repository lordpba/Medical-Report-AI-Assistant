import base64
import fitz  # PyMuPDF
import ollama
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main user interface page."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint to receive a file, process it, and get an analysis from Ollama.
    """
    try:
        # Retrieve data from the request
        file = request.files.get('file')
        model = request.form.get('model')
        prompt = request.form.get('prompt')
        content_type = request.form.get('contentType')

        if not all([file, model, prompt, content_type]):
            return jsonify({'error': 'Missing data in the request.'}), 400

        payload = {
            'model': model,
            'stream': False
        }

        # Process content based on its type
        if content_type == 'image':
            image_data = base64.b64encode(file.read()).decode('utf-8')
            payload['prompt'] = prompt
            payload['images'] = [image_data]
        
        elif content_type == 'images_array': # PDF case
            pdf_bytes = file.read()
            images_data = pdf_to_images_base64(pdf_bytes)
            payload['prompt'] = f"Analyze the following images, which represent the sequential pages of a single report. {prompt}"
            payload['images'] = images_data
            
        elif content_type == 'text':
            text_content = file.read().decode('utf-8')
            payload['prompt'] = f"Based on the following report, answer the question.\n\n---REPORT---\n{text_content}\n\n---QUESTION---\n{prompt}"
        
        else:
            return jsonify({'error': 'Invalid content type.'}), 400

        # Call Ollama
        client = ollama.Client()
        response = client.generate(**payload)

        return jsonify({'response': response['response']})

    except Exception as e:
        print(f"Error during analysis: {e}")
        return jsonify({'error': str(e)}), 500

def pdf_to_images_base64(pdf_bytes):
    """
    Converts a PDF file (in bytes) into a list of base64-encoded images.
    """
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    images_base64 = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(dpi=150) # Increase DPI for better quality
        img_bytes = pix.tobytes("jpeg")
        base64_string = base64.b64encode(img_bytes).decode('utf-8')
        images_base64.append(base64_string)
    return images_base64

if __name__ == '__main__':
    # Start the Flask server in debug mode
    app.run(debug=True, port=5000)

