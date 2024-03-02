import shutil
import time

from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

from import_xls import split_xls_files

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'input'
app.config['OUTPUT_FOLDER'] = 'output'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


if not os.path.exists(app.config['OUTPUT_FOLDER']):
    os.makedirs(app.config['OUTPUT_FOLDER'])


@app.route('/')
def index():
    return open('static/templates/index.html').read()


@app.route('/download/<tipe>/<filename>', methods=['GET'])
def download_file(tipe, filename):
    try:
        if tipe == 'folder':
            print(filename)
        return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        output_path1, output_path2 = split_xls_files(app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'])
        print(output_path1, output_path2)
        return jsonify({'output_filename1': os.path.basename(output_path1), 'output_filename2': os.path.basename(output_path2)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)