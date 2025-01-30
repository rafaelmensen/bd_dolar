import requests
import mysql.connector
from datetime import datetime
import certifi

def coletar_cotacao():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json"
    response = requests.get(url, verify=certifi.where())
    dados = response.json()

# Configurações do banco de dados
db_config = {
    'user': 'rafa',
    'password': 'rafa',
    'host': 'localhost',
    'database': 'cotacoes'
}

# Função para coletar cotações
def coletar_cotacao():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json"
    response = requests.get(url)
    dados = response.json()

    # Conectar ao banco de dados
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for item in dados:
        data = datetime.strptime(item['data'], '%d/%m/%Y').date()
        valor = float(item['valor'])
        fonte = "Banco Central do Brasil"

        # Inserir dados no banco
        cursor.execute("INSERT INTO cotacoes_dolar (data, valor, fonte) VALUES (%s, %s, %s)", (data, valor, fonte))

    conn.commit()
    cursor.close()
    conn.close()

# Chamar a função para coletar cotações
coletar_cotacao()
