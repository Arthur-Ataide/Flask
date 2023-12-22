# metodo HTTP: 
# GET -> obter dados
# POST -> enviar dados
# PUT -> atualizar dados
# DELETE -> deletar dados
# PATCH -> atualizar dados parcialmente

from flask import Flask, request
from json import dumps

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        print(request.form)
        # return 'OK POST nome: %s' % request.form['nome']
        return dumps(request.form)

    
    return 'OK GET'

if __name__ == '__main__':
    app.run(debug=True)