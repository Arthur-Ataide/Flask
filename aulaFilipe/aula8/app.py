# Redirecinamento e erros

from flask import Flask, abort, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='modelo.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['usuario'] == 'admin' and request.form['senha'] == 'admin':
            return redirect(url_for('sucesso'), code=302)
        
        abort(401)
    
    else:
        abort(403)

@app.route('/sucesso')
def sucesso():
    return 'Login com sucesso'

if __name__ == '__main__':
    app.run(debug=True)
    