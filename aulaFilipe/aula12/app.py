# upload de arquivos

import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
