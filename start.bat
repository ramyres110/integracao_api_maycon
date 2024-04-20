:: Script para execução do servidor
:: TODO: Verificar se existe o python antes de executar!
pip install -r requirements.txt
python integracao.py
IF %ERRORLEVEL% NEQ 0 Echo An error was found