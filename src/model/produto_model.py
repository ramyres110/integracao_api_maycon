from ..entidades.produto import Produto

QRY_SELECT = '''
            SELECT 
                CODIGO_INTERNO, 
                CODIGO_CATALOGO, 
                DESCRICAO, 
                FORNECEDOR, 
                SALDO, 
                PRECO_OPERACIONAL 
            FROM api_produtos
            '''

QRY_INSERT = '''
        INSERT INTO api_produtos(
            CODIGO_INTERNO, 
            CODIGO_CATALOGO, 
            DESCRICAO, 
            FORNECEDOR, 
            SALDO, 
            PRECO_OPERACIONAL
        )
        VALUES (?, ?, ?, ?, ?, ?)
        '''

# função com dicionário
def novo_produto(conn, dados):
    cursor = conn.cursor()
    values = (
        dados['codigo_interno'],
        dados['SKU'],
        dados['descricao'],
        dados['fornecedor'],
        int(dados['saldo']),
        float(dados['preco_operacional'].replace(',', '.'))
    )
    cursor.execute(QRY_INSERT, values)
    conn.commit()
    conn.close()

# Sugestão de mudança para objeto
def add_produto(conn, produto: Produto):
    cursor = conn.cursor()
    cursor.execute(QRY_INSERT, produto.asTuple())
    conn.commit()
    
# lista produtos cadastrados
def obter_produtos(conn):
    cursor = conn.cursor()
    res = cursor.execute(QRY_SELECT)
    tabela = res.fetchall()
    produtos = []
    for linha in tabela:
        produto = Produto(
            linha[0],# codigo_interno, 
            linha[1],# SKU, 
            linha[2],# descricao, 
            linha[3],# fornecedor,
            linha[4],# saldo, 
            linha[5],# preco_operacional
        )
        produtos.append(produto)
    return produtos


