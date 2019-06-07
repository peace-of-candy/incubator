from typing import Tuple
import doctest
import pandas as pd
import os
import zipfile
from os.path import abspath, dirname

def file_exists(path: str) -> bool:
    """
    :param path: can be either a filename or a directory name
    """
    return os.path.exists(path)

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

    name_and_unit = remove_characters(axis_label, '()').replace('_', ' ')
    name = ' '.join(name_and_unit.split(' ')[:-1])
    unit = name_and_unit.split(' ')[-1]

    return (name, unit)

def measurements_to_unit_map(df):
    measurements = filter(contains_unit_of_measurement, df.columns.values)

    return dict(map(name_and_unit_from_axis_label, measurements))

nutrient_data_url = 'https://www.ars.usda.gov/ARSUserFiles/80400525/Data/SR/SR28/dnload/sr28abxl.zip'
download_path = dirname(dirname(abspath(__file__))) + "/download"
nutrient_data_zip = download_path + "/ABBREV.zip"
nutrient_data_file = download_path + "/ABBREV.xlsx"

if not file_exists(download_path):
    os.makedirs(download_path)

# Downloads zip file, unzip and remove zip file.
if not file_exists(nutrient_data_file):
    urllib.request.urlretrieve(nutrient_data_url, nutrient_data_zip)
    zip_ref = zipfile.ZipFile(nutrient_data_zip, 'r')
    zip_ref.extractall(download_path)
    zip_ref.close()
    os.remove(nutrient_data_zip)

food_df = pd.read_excel(nutrient_data_file)