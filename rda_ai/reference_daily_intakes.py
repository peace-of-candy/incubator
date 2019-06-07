import doctest
import requests
import urllib.request

import pandas as pd

from typing import Tuple
from bs4 import BeautifulSoup

from micronutrients import is_micronutrient

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

def contains_unit_of_measurement(axis_label: str) -> bool:
    """
    An axis label is assumed to refer to contain a unit of measurement if it contains a per day "symbol" ('/d')

    :param axis_label: An axis label from a pandas dataframe
    :return: True if the axis label contains a unit of measurement, otherwise False
    """
    return '/d' in axis_label

def name_and_unit_from_axis_label(axis_label: str) -> Tuple[str, str]:
    """
    :param axis_label: A string on the form {micronutrient}_({unit}/d)

    >>> name_and_unit_from_axis_label('Calcium(mg/d)')
    ('Calcium', 'mg')
    """
    assert(contains_unit_of_measurement(axis_label))
    name_and_unit = axis_label.replace('/d)', '').split('(')

    return tuple(name_and_unit)

def measurement_name_from_axis_label(axis_label):
    return name_and_unit_from_axis_label(axis_label)[0]

def micronutrient_to_unit_map(df):
    micronutrients = filter(contains_unit_of_measurement, df.columns.values)

    return dict(map(name_and_unit_from_axis_label, micronutrients))

dietary_reference_intake_elements = get_dietary_reference_intakes(rda_ai_elements_url)
dietary_reference_intake_vitamins = get_dietary_reference_intakes(rda_ai_vitamins_url)

def micronutrients(columns):
    measurement_labels = filter(contains_unit_of_measurement, columns) # Contains unit
    measurement_names = map(measurement_name_from_axis_label, measurement_labels)
    micronutrients = filter(is_micronutrient, measurement_names)

    return list(micronutrients)

micros = micronutrients(dietary_reference_intake_elements.columns) + micronutrients(dietary_reference_intake_vitamins.columns)
print(micros)
