from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/teste', methods=['GET', 'POST'])
def teste():
    if request.method == 'GET':
        return jsonify({'mensagem': 'Usando Get'})
    
    elif request.method == 'POST':
        req_JSON = request.json
        name = req_JSON['name']
        return jsonify({'mensagem': f'Bem Vindo {name}!!'})
    
if __name__ == '__main__':
    app.run(debug=True, port = 9090)