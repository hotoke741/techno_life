import streamlit as st
from bs4 import BeautifulSoup
import requests

url = 'https://www.technolife.com/category/mobile/mobile-phone'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

descriptions = soup.select('section.relative.w-full h2')
for item in descriptions:
    print(item.get_text())
print('-'*30)

prices = soup.select('section.relative.w-full p.text-primary-shade-1')
for item in prices:
    print(item.get_text())
print('-'*30)

images = soup.select('section.relative.w-full img')

i = 0
for item in images:
    img_url = 'https://www.technolife.com' + item.get('src')
    
    with open(f'./images/mobiles/img_{i}.png', 'wb') as file:
        r  = requests.get(img_url).content
        file.write(r)
    i+=1