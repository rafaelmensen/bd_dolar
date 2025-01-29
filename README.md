# Banco de Dados Cotação do Dolar
Olá, esse é um estudo com base em alguns cursos sobre o estudo de banco de dados, estou usando a linguagem python com as seguintes importações de bibliotecas. 
```python
import requests
import sqlite3
import schedule
import time
import pandas as pd
import os
```
O objetivo realmente é voltado a entender melhor como funciona um banco de dados, a biblioteca ```requests``` é usanda para fazer aquisições ```HTTP``` para obter os dados de uma ```API```, ```sqlite3``` estou usando principalmente para ```interagir``` com o bd sqlite, ```schedule``` é voltada a ```função``` de ```tempo ou intervalos```, por exemplo quero agenda o mesmo para 1 minuto ou menos assim uso esse função dentro do jupyter como o exemplo abaixo.

```python
# Agendar a execução da função a cada minuto
schedule.every(1).minutes.do(save_cotacao)

# Loop para manter o agendamento
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)
```
Claro, tem as bibliotecas comuns como ```import pandas as pd``` e ```import os```, 
