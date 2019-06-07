import os
import zipfile
from os.path import abspath, dirname

nutrient_data_url = 'https://www.ars.usda.gov/ARSUserFiles/80400525/Data/SR/SR28/dnload/sr28abxl.zip'
download_path = dirname(dirname(abspath(__file__))) + "/download"
nutrient_data_zip = download_path + "/ABBREV.zip"
nutrient_data_file = download_path + "/ABBREV.xlsx"

if not os.path.exists(download_path):
    os.makedirs(download_path)

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


