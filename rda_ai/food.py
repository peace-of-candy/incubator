import functools

from macros import Macros
from container import Container
from rda_ai import get_in_gram
from micronutrients import is_vitamin, is_mineral


class Food:
    energy_kcal = 0
    energy_kj = 0  # Energy as container also with name Kj and kcal ? or function: kj = kcal * 4.184
    macros = Container("Macros")
    mineral = Container("Minerals")
    vitamins = Container("Vitamins")
    sugars = Container("Sugars")
    substance = Container("Substances")

    def __init__(self):
        self.substance.add_item("Water", 0.0)
        self.sugars.add_item("Sucrose", 0.0)
        self.sugars.add_item(("Fructose", "Glucose"), 0.0)
        self.sugars.add_item("Lactose", 0.0)
        self.sugars.add_item("Maltose", 0.0)
        self.macros.add_item("Protein", 0.0)
        self.macros.add_item("Carbohydrate", 0.0)
        self.macros.add_item("Protein", 0.0)

        fat = Container("Fats")
        fat.add_item("Saturated", 0.0)
        fat.add_item("Monounsaturated", 0.0)
        fat.add_item("Polyunsaturated", 0.0)
        fat.add_item("Trans", 0.0)
        self.macros.add_item("Fats", fat)

    def __str__(self):
        s = f"Energy: {self.energy_kcal}kcal /{self.energy_kj}kJ\n"
        s += str(self.macros)
        s += str(self.sugars)
        s += str(self.vitamins)
        s += str(self.mineral)
        s += str(self.substance)
        return s

    def add_item(self, name, value, unit):
        if is_vitamin(name):
            try:
                self.vitamins.add_item(name, get_in_gram(unit, value))
            except KeyError as e:
                print(f"Food, add_item, vitamins, KeyError, did add {name} with 0.0, cause: {e}")
                self.vitamins.add_item(name, 0.0)
        elif is_mineral(name):
            self.mineral.add_item(name, get_in_gram(unit, value))
        elif "Energy" in name:
            if unit == "kcal":
                self.energy_kcal = value
            elif unit == "kJ":
                self.energy_kj = value
        elif name in self.macros.get_names():
            self.macros.add_item(name, get_in_gram(unit, value))
        elif name in self.sugars.get_names():
            self.sugars.add_item(name, get_in_gram(unit, value))
        else:
            # print(f"Not added: {name} with {value}{unit}")
            pass

    def get_value(self, name: str) -> float:
        if is_vitamin(name):
            return self.vitamins.get_value(name) or 0.0
        elif is_mineral(name):
            self.mineral.get_value(name) or 0.0
        elif "kcal" == name:
            return self.energy_kcal
        elif name == "kJ":
            return self.energy_kj
        elif name in self.macros.get_names():
            return self.macros.get_value(name)
        elif name in self.sugars.get_names():
            return self.sugars.get_value(name)
        elif name in self.substance.get_names():
            return self.substance.get_value(name)
        else:
            raise ValueError(f"Didn't find {name} in the food.")
            pass


class SuperFood:

    def __init__(self, name=""):
        self.name = name
        self.foods = []

    def add(self, item, grams: float = 100.0):
        self.foods.append((item, grams))

    def get_value(self, name):
        # reduce should be able to do funcptr?
        # return functools.reduce(lambda a, b: a[0].get_value(name)*a[1] + b[0].get_value(name)*b[1], self.foods)
        sum = 0
        for (f, g) in self.foods:
            sum += (f.get_value(name) / 100.0) * g
        return sum
