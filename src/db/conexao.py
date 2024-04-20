import mysql.connector
import sqlite3
import os

# Conectar no bando de dados MySQUL
def conectar_mysql():
    '''
    Retorna uma conexão com o banco de dados.
    Local único de conexão para facilitar manutenção.
    '''
    config = {
        'user': os.getenv('DB_USER'), # Obtém o usuário do bando de dados que está na variável de ambiente
        'password': os.getenv('DB_PASSWORD'), # Obtém a senha do bando de dados que está na variável de ambiente
        'host': os.getenv('DB_HOST'), # Obtém o host do bando de dados que está na variável de ambiente
        'database': os.getenv('DB_DATABASE') # Obtém o nome do bando de dados que está na variável de ambiente
    }

    conn = mysql.connector.connect(**config) # faz a conexão no banco de dados
    return conn

def conectar_sqlite():
    db = sqlite3.connect('database.db')
    return db

def conectar_db():
    #TODO: Utilizar Parametrização para definir banco a ser utilizado
    return conectar_sqlite()