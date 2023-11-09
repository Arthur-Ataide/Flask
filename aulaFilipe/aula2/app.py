from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

def teste():
    return "<p>testando1</p>"

def teste2():
    return "<h1>testando2</h1>"

app.add_url_rule('/teste', 'teste', teste)
app.add_url_rule('/teste2', 'teste2', teste2)


if __name__ == '__main__':
    app.run(debug=True, port="4000")