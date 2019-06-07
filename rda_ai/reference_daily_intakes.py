from typing import Tuple
import doctest
import requests
import urllib.request
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

def is_micronutrient(axis_label: str) -> bool:
    """
    An axis label is assumed to refer to a micronutrient if it contains a per day "symbol" ('/d')

    :param axis_label: An axis label from a pandas dataframe
    :return: True if the axis label refers to a micronutrient, otherwise False
    """
    return '/d' in axis_label

def name_and_unit_from_axis_label(micronutrient_label: str) -> Tuple[str, str]:
    """
    :param micronutrient_label: A string on the form {micronutrient}_({unit}/d)

    >>> name_and_unit_from_axis_label('Calcium(mg/d)')
    ('Calcium', 'mg')
    """
    assert(is_micronutrient(micronutrient_label))
    name_and_unit = micronutrient_label.replace('/d)', '').split('(')

    return tuple(name_and_unit)

def micronutrient_to_unit_map(df):
    micronutrients = filter(is_micronutrient, df.columns.values)

    return dict(map(name_and_unit_from_axis_label, micronutrients))

dietary_reference_intakes_elements = get_dietary_reference_intakes(rda_ai_elements_url)
dietary_reference_intakes_vitamins = get_dietary_reference_intakes(rda_ai_vitamins_url)

