import os

from micronutrients import is_micronutrient, all_micronutrients, micronutrient_from_string

from usda import UsdaClient, UsdaNdbReportType

client = UsdaClient(os.environ['USDA_CLIENT_API_KEY'])
blueberries = next(client.search_foods('Blueberries, raw', 1))
walnuts = next(client.search_foods('Walnuts, raw', 1))
broccoli = next(client.search_foods('Broccoli, raw', 1))

seen_micronutrients = set()


def find_item(item: str, size: int = 10) -> list:
    foods_list = client.search_foods(item, size)
    l = ()
    for _ in range(size):
        food_item = next(foods_list)
        l += (food_item.id, food_item.name)
    return l


def get_nutrition_info(item: str) -> dict:
    food_stuff = next(client.search_foods(item, 1))
    report = client.get_food_report(food_stuff.id, report_type=UsdaNdbReportType.full)
    l = {}
    for nutrient in report.nutrients:
        nutrient_name = nutrient.name.split(',')[0].title()

        # Converts 'Vitamin B-6' to 'Vitamin B6'
        if 'Vitamin' in nutrient_name:
            nutrient_name = nutrient_name.replace('-', '')

        if is_micronutrient(nutrient_name):
            l[nutrient_name] = {}
            l[nutrient_name]["unit"] = nutrient.unit
            l[nutrient_name]["value"] = nutrient.value
    return l


# for food_stuff in [blueberries, walnuts, broccoli]:
#     report = client.get_food_report(food_stuff.id, report_type=UsdaNdbReportType.full)
#     print(food_stuff.name)
#     for nutrient in report.nutrients:
#         nutrient_name = nutrient.name.split(',')[0].title()
#
#         # Converts 'Vitamin B-6' to 'Vitamin B6'
#         if 'Vitamin' in nutrient_name:
#             nutrient_name = nutrient_name.replace('-', '')
#
#         if is_micronutrient(nutrient_name):
#             print(f'{nutrient_name} {nutrient.value} {nutrient.unit}')
#
#     print('')
#     print('')

#print(seen_micronutrients)
#print(set(all_micronutrients) - seen_micronutrients)


