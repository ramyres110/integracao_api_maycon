'''
Migrations são uma forma de controlar as alterações do 
schema (estrutura) do banco de dados de uma aplicação. 
Elas permitem criar, alterar ou remover tabelas, colunas, 
índices, chaves etc. e compartilhar essas mudanças com 
outros desenvolvedores
'''

# Apaga tabela api_produtos
def deletar_tabela_api_produtos(conn):
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE api_produtos;
    ''')

# Cria tabela api_produtos
def criar_tabela_api_produtos(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_produtos (
            CODIGO_INTERNO INT PRIMARY KEY,
            CODIGO_CATALOGO VARCHAR(255) NOT NULL,
            DESCRICAO VARCHAR(255) NOT NULL,
            FORNECEDOR VARCHAR(255) NOT NULL,
            SALDO INT,
            PRECO_OPERACIONAL DECIMAL(10,02)
        )
    ''')


# TODO: Adicionar campos de registro de tempo
def add_timestamps_tabela_api_produtos(conn):
    pass

# Executa todas as migrations
def executar_tudo(limpar: bool = False):
    if limpar:
        deletar_tabela_api_produtos()
    # Criações
    criar_tabela_api_produtos()
    # Alterações
    add_timestamps_tabela_api_produtos()