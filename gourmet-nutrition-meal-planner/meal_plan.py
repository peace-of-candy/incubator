from typing import List, Any
from dataclasses import dataclass, field
from recipe import Meal, Snack, green_cuisine_frittata, power_yoghurt, classy_chicken, eight_layer_dinner, apple_cinnamon_bar


@dataclass
class Day:
	name: str
	breakfast: Meal
	snack1: Snack
	lunch: Meal
	snack2: Snack
	dinner: Meal
	training_day: bool = True
	all_meals: List[Any] = field(init=False) 

	def __post_init__(self):
		self.all_meals = [self.breakfast, self.snack1, self.lunch, self.snack2, self.dinner]

	def calories(self):
		all_calories = map(lambda f: f.calories() if f else 0, self.all_meals)

		return sum(all_calories)

	def fats(self):
		return sum(map(lambda f: f.fat, self.all_meals))

	def protein(self):
		return sum(map(lambda f: f.protein, self.all_meals))

	def carbs(self):
		return sum(map(lambda f: f.carbs, self.all_meals))

	def __str__(self):
		def format_meal(meal):
			def format_name(meal):
				pw_label = " (PW)" if meal.postworkout else ""
				serving_size_label = f' ({meal.serving_size})' if meal.serving_size != 'L' else ""

				return f'{meal.name}{pw_label}{serving_size_label}'

			def format_macros(meal):
				return f'{list(map(str, meal.macros))}'

			return f'{format_name(meal)} {format_macros(meal)}'

		all_macros = [self.fats(), self.carbs(), self.protein()]
		aggregated_macros_pretty = list(map(str, all_macros))

		header = f'{self.name}: {aggregated_macros_pretty} => {self.calories()} calories'
		formatted_bits = [header]

		d = {
			'Breakfast': f'{format_meal(self.breakfast)}',
			'Snack 1': f'{format_meal(self.snack1)}',
			'Lunch': f'{format_meal(self.lunch)}',
			'Snack 2': f'{format_meal(self.snack2)}',
			'Dinner': f'{format_meal(self.dinner)}',
		}

		for k, v in d.items():
			k_with_colon = f'{k}:'
			formatted_bits.append(f'{k_with_colon:20}{v}')

		return '\n'.join(formatted_bits)

monday = Day(
	'Monday',
	green_cuisine_frittata,
	power_yoghurt,
	eight_layer_dinner,
	apple_cinnamon_bar.small(),
	classy_chicken)

print(monday)
