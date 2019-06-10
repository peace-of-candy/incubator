import doctest
import os
import urllib
import zipfile

import pandas as pd

from os.path import abspath, dirname
from typing import Tuple

from micronutrients import is_micronutrient

from utils.download import file_exists


def contains_unit_of_measurement(s: str) -> bool:
    return s.endswith('g)')

def name_and_unit_from_axis_label(axis_label: str) -> Tuple[str, str]:
    """
    >>> name_and_unit_from_axis_label('Carbohydrt_(g)')
    ('Carbohydrt', 'g')

    >>> name_and_unit_from_axis_label('Manganese_(mg)')
    ('Manganese', 'mg')

    >>> name_and_unit_from_axis_label('Vit_C_(mg)')
    ('Vit C', 'mg')
    """
    def remove_characters(s: str, chars: str):
        return ''.join([c for c in s if c not in chars])

    assert(contains_unit_of_measurement(axis_label))

    name_and_unit = remove_characters(axis_label, '()').replace('_', ' ')
    name = ' '.join(name_and_unit.split(' ')[:-1])
    unit = name_and_unit.split(' ')[-1]

    return (name, unit)

def measurement_name_from_axis_label(axis_label):
    return name_and_unit_from_axis_label(axis_label)[0]

def measurements_to_unit_map(df):
    measurements = filter(contains_unit_of_measurement, df.columns.values)

    return dict(map(name_and_unit_from_axis_label, measurements))

nutrient_data_url = 'https://www.ars.usda.gov/ARSUserFiles/80400525/Data/SR/SR28/dnload/sr28abxl.zip'
download_path = dirname(dirname(abspath(__file__))) + "/download"
nutrient_data_zip = download_path + "/ABBREV.zip"
nutrient_data_file = download_path + "/ABBREV.xlsx"


# Downloads zip file, unzip and remove zip file.
if not file_exists(nutrient_data_file):
    urllib.request.urlretrieve(nutrient_data_url, nutrient_data_zip)
    zip_ref = zipfile.ZipFile(nutrient_data_zip, 'r')
    zip_ref.extractall(download_path)
    zip_ref.close()
    os.remove(nutrient_data_zip)

food_df = pd.read_excel(nutrient_data_file)

# Rename all shorthand annotations for vitamins. So, for instance, turn 'Vit C' to 'Vitamin C'
food_df.rename(
    columns={c: c.replace('Vit', 'Vitamin') for c in food_df.columns},
    inplace=True)

# print(measurements_to_unit_map(food_df))

def micronutrients(columns):
    measurement_labels = filter(contains_unit_of_measurement, columns) # Contains unit
    measurement_names = map(measurement_name_from_axis_label, measurement_labels)
    micronutrients = filter(is_micronutrient, measurement_names)

    return list(micronutrients)

print(micronutrients(food_df.columns))
