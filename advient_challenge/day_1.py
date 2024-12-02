import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

# URL de la página
url = "https://adventofcode.com/2024/day/1/input"

# Realizar solicitud HTTP


cookies = {'session': '53616c7465645f5fc02ccbfd8050003a2754315bcc63506a413e7d72a66a45fdc180b5c16e573c1f2b5ce111dfdcbf989b60b3b4ffac1068b86f3e994fe02d2b'}

response = requests.get(url, cookies=cookies)

if response.status_code == 200:


    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    