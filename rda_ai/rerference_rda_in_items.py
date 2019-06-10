from reference_daily_intakes import get_elements_and_vitamins_in_groups

from nutrition_info_usda import get_nutrition_info

from rda_ai import convert_units


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


groups = get_elements_and_vitamins_in_groups()

# print(groups.keys())
# print(groups["Males"].keys())
male19to30 = groups["Males 19–30 y"]
# int(male19to30)
broc = get_nutrition_info('Broccoli, raw')

print("Compare (Males 19-30y) with (Broccoli, raw)")
get_rda_from_item(male19to30, broc)