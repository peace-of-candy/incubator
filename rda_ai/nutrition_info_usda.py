import os

from micronutrients import is_micronutrient, all_micronutrients, micronutrient_from_string

from usda import UsdaClient, UsdaNdbReportType

client = UsdaClient(os.environ['USDA_CLIENT_API_KEY'])
blueberries = next(client.search_foods('Blueberries, raw', 1))
walnuts = next(client.search_foods('Walnuts, raw', 1))
broccoli = next(client.search_foods('Broccoli, raw', 1))

seen_micronutrients = set()

for food_stuff in [blueberries, walnuts, broccoli]:
    report = client.get_food_report(food_stuff.id, report_type=UsdaNdbReportType.full)

    for nutrient in report.nutrients:
        nutrient_name = nutrient.name.split(',')[0]

        if is_micronutrient(nutrient_name):
            seen_micronutrients.add(micronutrient_from_string(nutrient_name))
        else:
            print(nutrient_name)

print(seen_micronutrients)
print(set(all_micronutrients) - seen_micronutrients)



