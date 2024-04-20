# import mysql.connector
#import requests
# from dotenv import load_dotenv
# import os
# import json
from flask import Flask, request
from .db.conexao import conectar_db
from .entidades.produto import Produto
from .model.produto_model import add_produto, obter_produtos


# def inserir_dados(conn, dados):
    # cursor = conn.cursor()

    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS api_produtos (
    #         CODIGO_INTERNO PRIMARY KEY,
    #         CODIGO_CATALOGO VARCHAR(255) NOT NULL,
    #         DESCRICAO VARCHAR(255) NOT NULL,
    #         FORNECEDOR VARCHAR(255) NOT NULL,
    #         SALDO INT,
    #         PRECO_OPERACIONAL DECIMAL(10,02)
    #     )
    # ''')
    # criar_tabela_api_produtos()

    # query = '''
    #     INSERT INTO api_produtos(
    #         CODIGO_INTERNO, CODIGO_CATALOGO, DESCRICAO, FORNECEDOR, SALDO, PRECO_OPERACIONAL
    #     )
    #     VALUE (%s, %s, %s, %s, %s, %s)
    # '''

    # values = (
    #     dados['codigo_interno'],
    #     dados['SKU'],
    #     dados['descricao'],
    #     dados['fornecedor'],
    #     int(dados['saldo']),
    #     float(dados['preco_operacional'].replace(',', '.'))
    # )

    # cursor.execute(query, values)
    # conn.commit()
    # novo_produto(conn, dados)


# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Rota para a requisião POST
@app.post('/api/v1/produtos')
def cadastrar_produtos():
    dados_cobol = request.get_json()
    
    #TODO: Sanitizar os dados recebidos!
    if type(dados_cobol) != list:
        return {"msg": 'Requisicao inválida'}, 400 

    #TODO: Remover prints para produção
    print(dados_cobol)

    conn = conectar_db()
    try:
        if dados_cobol:
            #TODO: Verificar necessidade de inserir varios!
            for dado in dados_cobol:
                produto: Produto = Produto(
                    dado['codigo_interno'].strip(),
                    dado['SKU'].strip(),
                    dado['descricao'].strip(),
                    dado['fornecedor'].strip(),
                    dado['saldo'].strip(),
                    dado['preco_operacional'].strip()
                )
                add_produto(conn, produto)
            
            #responder em JSON
            return {"msg": 'Dados inseridos no bando de dados com sucesso!'}, 201
        else:
            #responder em JSON
            return {"msg": 'Nenhum dado recebido.'}, 400

    except Exception as e:
        #TODO:
        print(e)
        conn.rollback()
        #responder em JSON
        return {"msg":f'Erro ao inserir dados: {str(e)}'}, 500
    finally:
        conn.close()


# Rota para a requisião POST
@app.get('/api/v1/produtos')
def listar_produtos():
    conn = conectar_db()
    produtos = obter_produtos(conn)
    conn.close()
    if len(produtos) > 0:
        produtos = [produto.asJson() for produto in produtos ]
    return produtos, 200

def run_servidor():
    # app.run(host= '192.9.200.212', port= 3500, debug= True)
    app.run(host= 'localhost', port= 3500, debug= True)


# Inicializa o aplicativo Flash na porta 3500 em mode de depuração
if __name__ == '__main__':
    run_servidor()
