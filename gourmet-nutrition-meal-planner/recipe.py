from typing import List, Any
from dataclasses import dataclass, field

def fmt_macro_total(macro_total, label):
	return f'{macro_total:.2f}{label}'

@dataclass
class Fats:
	# saturated: float = 0
	# monosaturated: float = 0
	# polyunsaturated: float = 0
	total: float = 0

	def __str__(self):
		return fmt_macro_total(self.total, 'f')

	def __add__(self, other):
		if (isinstance(other, Fats)):
			return Fats(self.total + other.total)
		else:
			return Fats(self.total + other)

	def __truediv__(self, scalar):
		return Fats(self.total/scalar)

	__radd__ = __add__

@dataclass
class Carbohydrates:
	# fiber: float = 0
	total: float = 0

	def __str__(self):
		return fmt_macro_total(self.total, 'c')

	def __add__(self, other):
		if (isinstance(other, Carbohydrates)):
			return Carbohydrates(self.total + other.total)
		else:
			return Carbohydrates(self.total + other)

	def __truediv__(self, scalar):
		return Carbohydrates(self.total/scalar)

	__radd__ = __add__

@dataclass
class Protein:
	total: float = 0

	def __str__(self):
		return fmt_macro_total(self.total, 'p')

	def __add__(self, other):
		if (isinstance(other, Protein)):
			return Protein(self.total + other.total)
		else:
			return Protein(self.total + other)

	def __truediv__(self, scalar):
		return Protein(self.total/scalar)

	__radd__ = __add__

F = Fats
C = Carbohydrates
P = Protein

@dataclass
class Recipe:
	name: str
	page: int
	fat: Fats 
	carbs: Carbohydrates
	protein: Protein 
	postworkout: bool = False
	macros: List[Any] = field(init=False)

	def __post_init__(self):
		self.macros = [self.fat, self.carbs, self.protein]

	def calories(self):
		# TODO: Move logic into each macro class
		return 9*float(self.fat.total) + 4*float(self.carbs.total) + 4*float(self.protein.total)

	def small(self):
		return Recipe(self.name, self.page, self.fat/2, self.carbs/2, self.protein/2, self.postworkout)

class Meal(Recipe):
	pass

class Snack(Recipe):
	pass

green_cuisine_frittata = Meal(
	name='Green-cuisine Frittata',
	page=48,
	fat=F(25),
	carbs=C(12),
	protein=P(47))

power_yoghurt = Snack(
	'Power Yoghurt',
	230,
	F(1.8),
	C(15.8),
	P(30))

eight_layer_dinner = Meal(
	'8-layer Dinner',
	125,
	F(15.4),
	C(75.8),
	P(56.3),
	postworkout=True)

apple_cinnamon_bar = Meal(
	'Apple Cinnamon Bar',
	228,
	F(38.2),
	C(17.9),
	P(25.1))

classy_chicken = Meal(
	'Classy Chicken',
	124,
	F(18.5),
	C(19.4),
	P(56.6))


	
