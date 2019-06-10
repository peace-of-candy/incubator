import re

import math
import pandas as pd
from typing import Tuple
from micronutrients import is_micronutrient
from utils.download import get_html

rda_ai_vitamins_url = 'https://www.ncbi.nlm.nih.gov/books/NBK56068/table/summarytables.t2/?report=objectonly'
rda_ai_elements_url = 'https://www.ncbi.nlm.nih.gov/books/NBK56068/table/summarytables.t3/?report=objectonly'
groups = {}



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
    >>> name_and_unit_from_axis_label('Calcium(mg/d)a')
    ('Calcium', 'mg')
    >>> name_and_unit_from_axis_label('Calcium(mg/d)a,b')
    ('Calcium', 'mg')
    """
    assert(contains_unit_of_measurement(axis_label))
    name_and_unit = axis_label.split('/d)')[0].split('(')

    return tuple(name_and_unit)

def measurement_name_from_axis_label(axis_label):
    return name_and_unit_from_axis_label(axis_label)[0]

def measurement_unit_from_axis_label(axis_label):
    return name_and_unit_from_axis_label(axis_label)[1]

def micronutrient_to_unit_map(df):
    micronutrients = filter(contains_unit_of_measurement, df.columns.values)

    return dict(map(name_and_unit_from_axis_label, micronutrients))


def micronutrients(columns):
    measurement_labels = filter(contains_unit_of_measurement, columns) # Contains unit
    measurement_names = map(measurement_name_from_axis_label, measurement_labels)
    micronutrients = filter(is_micronutrient, measurement_names)
    return list(micronutrients)


def get_elements_and_vitamins_in_groups():
    if 0 < len(groups):
        return groups
    last = ""
    for index, row in dietary_reference_intake_elements.iterrows():
        if isinstance(row[1], float) and math.isnan(float(row[1])):
            last = row[0]
        else:
            current = "{} {}".format(last, row[0])
            c = groups[current] = {}
            for colname in dietary_reference_intake_elements.columns[1:]:
                clean_colname = measurement_name_from_axis_label(colname)
                unit = measurement_unit_from_axis_label(colname)
                c[clean_colname] = {}
                c[clean_colname]["unit"] = unit
                c[clean_colname]["value"] = float(re.findall(r"[-+]?\d*\.\d+|\d+", row[colname])[0])
                cat: str = "RDA"
                if "*" in row[colname]:
                    cat = "AI"
                c[clean_colname]["category"] = cat


    for index, row in dietary_reference_intake_vitamins.iterrows():
        if isinstance(row[1], float) and math.isnan(float(row[1])):
            groups[row[0]] = {}
            last = row[0]
        else:
            current = "{} {}".format(last, row[0])
            c = groups[current]
            for colname in dietary_reference_intake_vitamins.columns[1:]:
                clean_colname = measurement_name_from_axis_label(colname)
                unit = measurement_unit_from_axis_label(colname)
                c[clean_colname] = {}
                c[clean_colname]["unit"] = unit
                c[clean_colname]["value"] = float(re.findall(r"[-+]?\d*\.\d+|\d+", row[colname])[0])
                cat: str = "RDA"
                if "*" in row[colname]:
                    cat = "AI"
                c[clean_colname]["category"] = cat

    return groups


dietary_reference_intake_elements = get_dietary_reference_intakes(rda_ai_elements_url)
dietary_reference_intake_vitamins = get_dietary_reference_intakes(rda_ai_vitamins_url)

if __name__ == "__main__":
    print("Main")
    #print("Micros")
    #micros = micronutrients(dietary_reference_intake_elements.columns) + micronutrients(dietary_reference_intake_vitamins.columns)
    #print(get_dietary_reference_intakes_for_males())

