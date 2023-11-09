from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<nome>')
def index(nome=''):
    return '<h1>Hello {}!!</h1>'.format(nome)

@app.route('/blog/')
@app.route('/blog/<float:postID>')
def blog(postID=0):
    if postID == 0:
        return 'Blog todo'
    else:
        return 'Blog info {}'.format(postID)

if __name__ == '__main__':
    app.run(debug=True, port="4000")