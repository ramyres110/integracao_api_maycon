from flask import Flask, request
import json

# Cria uma instância do aplicativo Flash
app = Flask(__name__)

# Rota com a requisições POST
@app.route('/api/v1/produtos', methods=['POST'])
def produtos():

    dados_cobol = request.get_json()
    print(dados_cobol)

    # Formata os dados em JSON com indentação
    dados_formatados = json.dumps(dados_cobol, indent=4)

    # Escreve os dados formatados em um arquivo de texto
    with open("dados_cobol.txt", 'a') as file:
        file.write(dados_formatados + '\n\n')

    # Retorna 'ok' como resposta para a requisição
    return 'ok'

# Inicializa o aplicativo Flash na porta 3500 em modo de depuração
if __name__ == '__main__':
    app.run(host= '192.9.200.212', port= 3500, debug=True)