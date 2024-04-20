#!\bin\python3
#-*- coding: utf-8 -*-
from dotenv import load_dotenv
from src.api_produto import run_servidor
from src.db.migration import criar_tabela_api_produtos
from src.db.conexao import conectar_db

load_dotenv()


if __name__ == "__main__":
    criar_tabela_api_produtos(conectar_db())
    run_servidor()