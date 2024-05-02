# upload de arquivos

import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    
    file = request.files['image']
    file.save(os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)))
    return "Upload realizado com sucesso!"


@app.route('/get-image/<filename>')
def get_image(filename):
    # return send_from_directory(UPLOAD_FOLDER, filename + '.png') # aqui mostra a imagem
    # return send_file(os.path.join(UPLOAD_FOLDER, filename + '.png'), as_attachment=True) # aqui baixa a imagem
    # return send_file(os.path.join(UPLOAD_FOLDER, filename + '.png'), mimetype='image/png') # aqui mostra a imagem
    return ""

if __name__ == '__main__':
    app.run(debug=True)
