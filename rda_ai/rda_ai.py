import os
import zipfile
from os.path import abspath, dirname

import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def name(item):
    return ' '.join(item.split('_')[:-1])

def unit(item):
    return item.split('_')[-1].replace('(', '').replace(')', '')

print(name('Vit_C_(mg)'))
print(unit('Vit_C_(mg)'))

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
# dict(map(tuple, list(filter(lambda l: len(l) == 2, [s.split('/d)')[0].split('(') for s in b.index.values]))))
rda_elements_to_unit_map = {'Calcium': 'mg', 'Chromium': 'μg', 'Copper': 'μg', 'Fluoride': 'mg', 'Iodine': 'μg', 'Iron': 'mg', 'Magnesium': 'mg', 'Manganese': 'mg', 'Molybdenum': 'μg', 'Phosphorus': 'mg', 'Selenium': 'μg', 'Zinc': 'mg', 'Potassium': 'g', 'Sodium': 'g', 'Chloride': 'g'}
rda_vitamins_to_unit_map = {'Vitamin A': 'μg', 'Vitamin C': 'mg', 'Vitamin D': 'μg', 'Vitamin E': 'mg', 'Vitamin K': 'μg', 'Thiamin': 'mg', 'Riboflavin': 'mg', 'Niacin': 'mg', 'Vitamin B6': 'mg', 'Folate': 'μg', 'Vitamin B12': 'μg', 'Pantothenic Acid': 'mg', 'Biotin': 'μg', 'Choline': 'mg'}


nutrient_data_url = 'https://www.ars.usda.gov/ARSUserFiles/80400525/Data/SR/SR28/dnload/sr28abxl.zip'
download_path = dirname(dirname(abspath(__file__))) + "/download"
nutrient_data_zip = download_path + "/ABBREV.zip"
nutrient_data_file = download_path + "/ABBREV.xlsx"

if not os.path.exists(download_path):
    os.makedirs(download_path )

# Downloads zip file, unzip and remove zip file.
if not os.path.exists(nutrient_data_file):
    urllib.request.urlretrieve(nutrient_data_url, nutrient_data_zip)
    zip_ref = zipfile.ZipFile(nutrient_data_zip, 'r')
    zip_ref.extractall(download_path)
    zip_ref.close()
    os.remove(nutrient_data_zip)

food_df = pd.read_excel(nutrient_data_file)

def get_nutrient_data(df, item):
    return df.loc[df['Shrt_Desc'] == item]


df_broccoli = get_nutrient_data(food_df, "BROCCOLI,RAW")
df_blueberries = get_nutrient_data(food_df, "BLUEBERRIES,RAW")
df_walnuts = get_nutrient_data(food_df, "WALNUTS,ENGLISH")
# dict(map(tuple, sorted(list(filter(lambda l: len(l) == 2, [s.replace(')', '').replace("_"," ").split(' (') for s in fdfh])))))
neutrient_to_unit_map = {'Alpha Carot': 'µg', 'Ash': 'g', 'Beta Carot': 'µg', 'Beta Crypt': 'µg', 'Calcium': 'mg', 'Carbohydrt': 'g', 'Cholestrl': 'mg', 'Choline Tot ': 'mg', 'FA Mono': 'g', 'FA Poly': 'g', 'FA Sat': 'g', 'Fiber TD': 'g', 'Folate DFE': 'µg', 'Folate Tot': 'µg', 'Folic Acid': 'µg', 'Food Folate': 'µg', 'Iron': 'mg', 'Lipid Tot': 'g', 'Lut+Zea ': 'µg', 'Lycopene': 'µg', 'Magnesium': 'mg', 'Manganese': 'mg', 'Niacin': 'mg', 'Phosphorus': 'mg', 'Potassium': 'mg', 'Protein': 'g', 'Retinol': 'µg', 'Riboflavin': 'mg', 'Selenium': 'µg', 'Sodium': 'mg', 'Sugar Tot': 'g', 'Thiamin': 'mg', 'Vit B12': 'µg', 'Vit B6': 'mg', 'Vit C': 'mg', 'Vit E': 'mg', 'Vit K': 'µg', 'Water': 'g', 'Zinc': 'mg'}

#print(df_broccoli)
#print(df_blueberries)
#print(df_walnuts)


def convert_units(given_unit):
    """

    :param given_unit:
    :return: 10^x from base.
    """
    given_unit = given_unit.replace("μ", "MICRO")
    given_unit = given_unit.replace("µ", "MICRO") #DIFF!
    #assert given_unit[-1] == "g"

    prefix = {"M": 6, "k": 3, "h": 2, "d": -1, "c": -2, "m": -3, "MICRO": -6, "n": -9, "p": -12, "f": -15, "a": -18, "z": -21, "y": -24}
    print("given unit: {}".format(given_unit))
    if given_unit == "g":
        return 0
    return prefix[given_unit[:-1]]

#union all = ['Alpha Carot', 'Ash', 'Beta Carot', 'Beta Crypt', 'Biotin', 'Calcium', 'Carbohydrt', 'Chloride', 'Cholestrl', 'Choline', 'Choline Tot ', 'Chromium', 'Copper', 'FA Mono', 'FA Poly', 'FA Sat', 'Fiber TD', 'Fluoride', 'Folate', 'Folate DFE', 'Folate Tot', 'Folic Acid', 'Food Folate', 'Iodine', 'Iron', 'Lipid Tot', 'Lut+Zea ', 'Lycopene', 'Magnesium', 'Manganese', 'Molybdenum', 'Niacin', 'Pantothenic Acid', 'Phosphorus', 'Potassium', 'Protein', 'Retinol', 'Riboflavin', 'Selenium', 'Sodium', 'Sugar Tot', 'Thiamin', 'Vit B12', 'Vit B6', 'Vit C', 'Vit E', 'Vit K', 'Vitamin A', 'Vitamin B12', 'Vitamin B6', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Water', 'Zinc']
#neutrient_to_unit_map intersect rda_vitamins_to_unit_map = {'Iron', 'Zinc', 'Sodium', 'Selenium', 'Calcium', 'Magnesium', 'Potassium', 'Phosphorus', 'Manganese'}
#neutrient_to_unit_map intersect rda_elements_to_unit_map = {'Niacin', 'Thiamin', 'Riboflavin'}

