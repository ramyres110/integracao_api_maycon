import mysql.connector
from dotenv import load_dotenv
import os
import requests

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Conecta no bando de dados MySQL
def conectar_mysqul():
    config = {
        'user': os.getenv('DB_USER'), # Obtém o user do bando de dados na variável de ambiente .env
        'password': os.getenv('DB_PASSWORD'), # Obtém o password do banco de dados na variável de ambiente .env
        'host': os.getenv('DB_HOST'), # Obtém o host do banco de dados na variável de ambiente .env
        'database': os.getenv('DB_DATABASE') # Obtém o database do bando de dados na variável de ambiente .env
    }

    conn = mysql.connector.connect(**config) # Faz a conexão no banco de dados
    return conn

def busca_metrica(conn):
    url = 'http://localhost:3500/api/v1/produtos'

    retorno = requests.get(url)
    retorno.raise_for_status()
    print(retorno.status_code) # Verifica se o status retornou 'ok'

    if retorno.status_code == 200:
        dados = retorno.json()

        for resultado in dados:
            codigo_interno = resultado['codigo_interno']
            codigo_catalogo = resultado['SKU']
            descricao = resultado['descricao']
            fornecedor = resultado['fornecedor']
            saldo = resultado['saldo']
            preco_operacional = resultado['preco_operacional']
            print(retorno.json)

        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXITS api_produtos (
                CODIGO_INTERNO PRIMARY KEY,
                CODIGO_PRODUTO VARCHAR(255) NOT NULL,
                DESCRICAO VARCHAR(255) NOT NULL,
                FORNECESOR VARCHAR(255) NOT NULL,
                SALDO INT,
                PRECO_OPERACIONAL DECIMAL(10,2)
            )
        ''')

        quey = '''
            INSERT INT PRODUTOS(
                CODIGO_INTERNO, CODIGO_CATALOGO, DESCRICAO, FORNECESOR, SALDO, PRECO_OPERACIONAL
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        '''

        values = (
            codigo_interno, codigo_catalogo, descricao, fornecedor, saldo, preco_operacional
        )

        cursor.execute(quey, values)
        conn.commit()

#conn = conectar_mysqul()
#busca_metrica(conn)