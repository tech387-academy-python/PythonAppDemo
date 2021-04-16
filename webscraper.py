from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests, json

def scrapCars():
    
    source = requests.get('https://www.izmostock.com/car-stock-photos-by-brand').text

    soup = BeautifulSoup(source, 'lxml')

    my_table = soup.find('div', {'id': 'page-content'})

    links = my_table.findAll('span')

    cars = []

    for link in links:
        cars.append(link.text)     
        
    with open ('data.json', 'w', encoding='utf-8') as f:
        json.dump(cars, f, ensure_ascii=False, indent=4)
