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
Claro, tem as bibliotecas comuns como ```import pandas as pd``` que estou ultilizando para manipular dados em parquet e ```import os``` para o uso de criação de arquivos e leitura dos mesmo como o exemplo abaixo.

```python
# Definindo o diretório
diretorio = r'C:\Git\USER\testes\Chamados\BANCO DOLAR TESTE'
```
# Inicio #

Vamos iniciar usando a linguagem python dentro do seu vscode, lembre-se antes de instalar o python no seu computador e claro as extensões dentro do vscode. Nesse inicio vamos criar uma pasta com o nome Banco de Dados, após a criação dentro do vscode, la em cima no canto esquerdo você seleciona a opção de ```File - Open Folder```, nela procura o caminho da pasta e realiza a abertura da mesma. 

# Diretório #
A ideia do projeto é ler dados de a cada 1 minuto da cotação do dolar e no final exportar como arquivo parquet, visando o controle do mesmo, desde a criação de um dash ou até mesmo outro tipo de analise. 

Vamos iniciar importando a biblioteca e depois o caminho do diretorio, para isso crie um new file com o nome, ```banco_dolar.ipynb```, onde vamos executar um jupyter que usamos para ler linhas e deixar as mesmas armazenadas em cache. 

```python

import requests
import sqlite3
import schedule
import time
import pandas as pd
import os

diretorio = r'C:\Git\BI0730\testes\Chamados\BANCO DOLAR TESTE'
```






































































exucutar abaixo para fazer o commit 

cd C:\rafa\bd_dolar
git add .
git status
git commit -m "Adicionando arquivos não rastreados"
git push origin main







