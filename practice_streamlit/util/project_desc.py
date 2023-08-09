import streamlit as st
import os, re
import urllib.request as ur
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd


url = 'https://www.chicagomag.com/chicago-magazine/january-2023/our-30-favorite-things-to-eat-right-now/'
hdr = {'User-Agent' : 'Mozilla/5.0'}
req = Request(url, headers = hdr)
page = urlopen(req)

soup = bs(page, 'html.parser')
soup.find_all('div', 'article-body')
tmp = soup.find_all('div','article-body')[0]

food_list = []
for item in tmp.find_all('h2'):
    food_list.append(item.text)

restaurant_list = []
for item in tmp.find_all('h3'):
    restaurant_list.append(item.text[3:])

money_list = []
address_list = []
for item in tmp.find_all('p'):
    sample_text = item.text
    idx_of_dollar = sample_text.index('$')
    money = sample_text[idx_of_dollar:].split('. ',1)[0].strip('.')
    dummy_address = sample_text[idx_of_dollar+len(money)+2:]
    money_list.append(money)
    address_list.append(dummy_address)

data = [list(item) for item in zip(food_list, restaurant_list, money_list, address_list)]
df = pd.DataFrame(data, columns = ['food','restaurant','price','address'])

def desc():
    global df
    st.dataframe(df)