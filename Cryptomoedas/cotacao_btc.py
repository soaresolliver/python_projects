# -*- coding: utf-8 -*-
"""Cotacao_btc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15yIbCC3e1Dud2nwWNquP0QDL9Ute5Ecv
"""

import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
dic_requisicao = requisicao.json()
df = (dic_requisicao)
df