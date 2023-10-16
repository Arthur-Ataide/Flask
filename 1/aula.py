from flask import Flask, render_template

app = Flask(__name__)

# crair a 1° pag do site

# route -> arthursite/ ... arthursite.com/usuario ... /contatos -> ou seja o caminho do site
# funçao -> o qe quero exibir na página
# template


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome = nome_usuario)


# colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)

