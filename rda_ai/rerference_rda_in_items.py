import re

from reference_daily_intakes import get_elements_and_vitamins_in_groups

from nutrition_info_usda import get_nutrition_info

from rda_ai import convert_units
from food import Food, SuperFood


def get_rda_from_item(group, item):
    for nutrient_name, nutrient_value in group.items():
        if nutrient_name in item:
            try:
                gnv = pow(10, convert_units(nutrient_value["unit"])) * nutrient_value["value"]
                inv = pow(10, convert_units(item[nutrient_name]["unit"])) * item[nutrient_name]["value"]
                # inv = item[nutrient_name]["value"]
                # inu = item[nutrient_name]["unit"]
                in_percent = (inv / gnv)*100.0
                print(f"{nutrient_name.ljust(20)} {gnv:.2f}g vs {inv:.2f}g ({in_percent:.1f}%)")
            except KeyError as e:
                print(f"{nutrient_name.ljust(20)} N/A (cause of convert error - {e})")
        else:
            print(f"{nutrient_name.ljust(20)} N/A (cause: Nutrient not specified in the given item)")


def get_food_from_usda_item(item, replace=[], replace_with=[]):
    f = Food()
    for n, val in item.items():
        name = n
        if name in replace:
            name = replace_with[replace.index(name)]
        elif re.fullmatch("^\d+:\d+$", name):
            # This is fats.
            fattytype = name.split(":")[1]
            if fattytype == "0":
                name = "Saturated"
            elif fattytype == "1":
                name = "Monounsaturated"
            elif fattytype == "2":
                name = "Polyunsaturated"
            elif fattytype == "3":
                name = "Trans"
        f.add_item(name, val["value"], val["unit"])
    return f

groups = get_elements_and_vitamins_in_groups()
male19to30 = groups["Males 19–30 y"]

sf = SuperFood()
r = ['Energy', 'Protein', 'Carbohydrate, by difference', 'Sucrose', 'Glucose (Dextrose)', 'Fructose', 'Lactose', 'Maltose']#, 'Fatty acids, total monounsaturated', 'Fatty acids, total polyunsaturated', 'Fatty acids, total trans', 'Fatty acids, total saturated']
rw = ['Energy', 'Protein', 'Carbohydrate', 'Sucrose', 'Glucose', 'Fructose', 'Lactose', 'Maltose']#, 'Monounsaturated', 'Polyunsaturated', 'Trans', 'Saturated']

broc_usda = get_food_from_usda_item(get_nutrition_info('Broccoli, raw'), r, rw)
blue_usda = get_food_from_usda_item(get_nutrition_info('Blueberries, raw'), r, rw)
wal_usda = get_food_from_usda_item(get_nutrition_info('Walnuts, raw'), r, rw)

sf.add(broc_usda)
sf.add(blue_usda)
sf.add(wal_usda)


for t in ['Saturated', 'kcal']:
    print(f"Broc {t}: {broc_usda.get_value(t)}")
    print(f"blue {t}: {blue_usda.get_value(t)}")
    print(f"Wal {t}: {wal_usda.get_value(t)}")
    print(f"All {t}: {sf.get_value(t)}")


#print(broc)
#print("Compare (Males 19-30y) with (Broccoli, raw)")
#get_rda_from_item(male19to30, broc)
