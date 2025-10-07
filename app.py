from flask import Flask, request, jsonify, render_template
import ollama
import base64
import fitz  # PyMuPDF
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    start_time = time.time()
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    model = request.form.get('model')
    prompt = request.form.get('prompt')
    content_type = request.form.get('contentType')

    if not all([file, model, prompt, content_type]):
        return jsonify({'error': 'Missing data in the request (file, model, prompt, or contentType)'}), 400

    images_base64 = []
    
    try:
        if content_type == 'image':
            image_bytes = file.read()
            images_base64.append(base64.b64encode(image_bytes).decode('utf-8'))
        elif content_type == 'images_array': # PDF processing
            pdf_bytes = file.read()
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            for page in doc:
                pix = page.get_pixmap(dpi=150)
                img_bytes = pix.tobytes("jpeg")
                images_base64.append(base64.b64encode(img_bytes).decode('utf-8'))
            doc.close()
        elif content_type == 'text':
            text_content = file.read().decode('utf-8')
            prompt = f"Based on the following report, answer the question.\n\n---REPORT---\n{text_content}\n\n---QUESTION---\n{prompt}"
        else:
             return jsonify({'error': f'Unsupported content type: {content_type}'}), 400
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500

    try:
        payload = {'model': model, 'prompt': prompt, 'stream': False}
        if images_base64:
            payload['images'] = images_base64

        response = ollama.generate(**payload)
        
        end_time = time.time()
        total_duration = round(end_time - start_time, 2)
        eval_duration_ns = response.get('eval_duration', 1)
        eval_count = response.get('eval_count', 0)
        tokens_per_second = round(eval_count / (eval_duration_ns / 1_000_000_000), 2) if eval_duration_ns > 0 else 0

        stats = {
            'total_duration': total_duration,
            'token_count': eval_count,
            'tokens_per_second': tokens_per_second
        }

        return jsonify({'response': response['response'], 'stats': stats})
    except Exception as e:
        return jsonify({'error': f'Error during analysis: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)

