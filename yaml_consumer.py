from yaml import load
from yaml.loader import Loader
import requests
from bs4 import BeautifulSoup as bsoup
from railwire_test import response_soup

def get_text(selector):
    text = from_soup(selector)
    stripped_text = text.strip()
    return stripped_text

def from_soup(selector):
    return response_soup.select(selector)[0].get_text()


data_dict = {}
with open("railwire.yml", 'r', encoding="utf-8") as stream:
    dictionary = load(stream, Loader=Loader)
    keys = [x for x in dictionary["scraping_data"].keys()] 
    for key in keys:
        if dictionary["scraping_data"][key]["tag"]  != "none":
            print(f'{get_text(dictionary["scraping_data"][key]["tag"]["selector"])}')
        