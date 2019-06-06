import requests
from bs4 import BeautifulSoup
import pandas as pd

rda_ai_vitamins_url = 'https://www.ncbi.nlm.nih.gov/books/NBK56068/table/summarytables.t2/?report=objectonly'
rda_ai_elements_url = 'https://www.ncbi.nlm.nih.gov/books/NBK56068/table/summarytables.t3/?report=objectonly'

def get_html(url):
    return requests.get(url).text

def get_all_tables(url):
    return pd.read_html(get_html(url))

def get_dietary_reference_intakes(url):
    return get_all_tables(url)[0]

def get_dietary_reference_intakes_for_males():
    return (get_dietary_reference_intakes(rda_ai_elements_url).iloc[9,:], get_dietary_reference_intakes(rda_ai_vitamins_url).iloc[9,:])

print(get_dietary_reference_intakes_for_males())



