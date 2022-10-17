import time
from flask import Flask,render_template, request
from flask_cors import CORS
import subprocess
import os
from main import highlight_translations

app = Flask(__name__)
CORS(app)

@app.route('/edit', methods=['POST'])
def edit_file():
    if  not request.files['file']:
        return 'no file was uploaded'
    else:
        file_to_upload = request.files['file']
        filename = request.files['filename'].read().decode("utf-8")
        fname = filename.split('.')[0]
        # fileFormat = filename.split('.')[1]
        highlight_result = highlight_translations(file_to_upload,fname)
        return highlight_result

        


@app.route('/open')
def just_text():
    path = os.path.normpath(os.path.expanduser("~/highlighted_files"))
    subprocess.Popen(r'explorer /select,' + path)
    return "opened"

