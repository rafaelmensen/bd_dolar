# bd_dolar
Banco Cotação Dolar voltado a estudo de banco de dados, estou usando a linguagem python com as seguintes importações de bibliotecas. 
//
import requests
import sqlite3
import schedule
import time
import pandas as pd
import os
//
O objetivo realmente é voltado a entender melhor como funciona um bd de dolar, a biblioteca requests é usanda para fazer aquisições HTTP para obter os dados de uma API, sqlite3 estou usando principalmente para interagir com o bd sqlite, schedule é voltada a função de tempo ou intervalos, por exemplo quero agenda o mesmo para 1 minuto ou menos assim uso esse função dentro do jupyter

# Agendar a execução da função a cada minuto
schedule.every(1).minutes.do(save_cotacao)

# Loop para manter o agendamento
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)
