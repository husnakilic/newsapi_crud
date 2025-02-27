# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dLCIBDIyDSAzsBRwi9onElLVhJiEL8mV
"""

API_KEY = '434d18af4a40454f95386a3e39b174ec'

import requests

def get_news(query, language="tr"):
    url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["articles"] if "articles" in data else []

haberler = get_news("teknoloji")
for haber in haberler[:5]:  # İlk 5 haberi yazdıralım
    print(haber["title"])