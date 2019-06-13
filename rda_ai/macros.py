from container import Container


class Macros:

    def __init__(self):
        self.protein = 0.0
        self.carbohydrate = 0.0
        self.fat = Container("Fats")
        self.fat.add_item("Saturated", 0.0)
        self.fat.add_item("Monounsaturated", 0.0)
        self.fat.add_item("Polyunsaturated", 0.0)
        self.fat.add_item("Trans", 0.0)

    def __str__(self):
        s = f"Macros ({self.get_totals()})\n"
        s += f" - Proteins: {self.protein}\n"
        s += f" - Carbohydrate: {self.carbohydrate}\n"
        s += " - " + str(self.fat).replace("\n", "\n  ")
        return s[:-2] # otherwise next str gets spaced.

    def get_totals(self):
        return self.protein + self.carbohydrate + self.fat.get_totals()

    def get_macro_names(self):
        return ["Protein", "Carbohydrate"] + list(map(lambda x : f"{x}", self.fat.get_names()))  # f"{x} (Fat)"

    def add(self, name, value):
        if name is "Protein":
            self.protein = value
        if name is "Carbohydrate":
            self.carbohydrate = value
        if name in self.fat.get_names():
            self.fat.add_item(name, value)

    def get_value(self, name):
        if name is "Protein":
            return self.protein
        if name is "Carbohydrate":
            return self.carbohydrate
        if name in self.fat.get_names():
            return self.fat.get_value(name)
        if "name" == "Fats":
            return self.fat.get_totals()

