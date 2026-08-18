from flask import Flask, render_template, request
import os
import cv2
from image_processing import *

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['image']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filepath)

    return render_template(
        'index.html',
        original=file.filename,
        processed=file.filename
    )

if __name__ == '__main__':
    app.run(debug=True)
    
    import shutil

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['image']

    if file.filename == '':
        return "No file selected"

    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    processed_path = os.path.join(app.config['PROCESSED_FOLDER'], file.filename)

    file.save(upload_path)

    # Copy uploaded image to processed folder initially
    shutil.copy(upload_path, processed_path)

    return render_template(
        'index.html',
        original=file.filename,
        processed=file.filename
    )