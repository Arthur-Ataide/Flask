# Banco de dados

from flask import Flask, render_template, request, redirect, url_for, Response
from models import db, Estudante
import json

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'


@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    idade = request.form['idade']
    estudante = Estudante(nome, idade)
    db.session.add(estudante)
    db.session.commit()
    return app.response_class(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")

# @app.route('/edit/<int:id>', methods=['POST', 'GET'])
# def edit(id):
#     estudante = Estudante.query.get(id)
#     if request.method == 'POST':
#         nome = request.form['nome']
#         idade = request.form['idade']
#         estudante.nome = nome
#         estudante.idade = idade
#         db.session.commit()
#         return app.response_class(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")
#     else:
#         # código para o método GET aqui

@app.route('/edit/<int:id>', methods=['POST', 'PUT'])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['DELETE', 'GET'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)