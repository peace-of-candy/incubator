from enum import Enum
import itertools

# The B-vitamins and their alternate names
b_vitamins = {
    'Vitamin_B1': ['Thiamin', 'Thiamine'],
    'Vitamin_B2': ['Riboflavin'],
    'Vitamin_B3': ['Niacin'],
    'Vitamin_B5': ['Pantothenic Acid'],
    'Vitamin_B6': ['Pyridoxine'],
    'Vitamin_B7': ['Biotin'],
    'Vitamin_B9': ['Folate', 'Folic Acid'],
    'Vitamin_B12': ['Cobalamin'],
}

# Allow B-vitamins to be self-referential (i.e., Vitamin B1 is a key for Vitamin B1)
b_vitamins = {k: [k] + v for k, v in b_vitamins.items()}
assert(b_vitamins['Vitamin_B1'] == ['Vitamin_B1', 'Thiamin', 'Thiamine'])

other_vitamins = [
    'Vitamin_A', 
    'Vitamin_C', 
    'Vitamin_D', 
    'Vitamin_E', 
    'Vitamin_K', 
    'Choline']

# Allow all the other vitamins to be self-referential too,
other_vitamins = {v: [v] for v in other_vitamins}

def join_dictionaries(d1, d2):
    return {**d1, **d2}

all_vitamins = join_dictionaries(b_vitamins, other_vitamins)

# Map 'Vitamin_A' to 'Vitamin A' as well (no underscore). Remove duplicates using set
all_vitamins = {k: list(set([k.replace('_', ' ')] + v)) for k, v in all_vitamins.items()}
assert(set(all_vitamins['Vitamin_A']) ==  set(['Vitamin A', 'Vitamin_A'])) # Using set to not care about order
assert(all_vitamins['Choline'] == ['Choline']) # No duplicates

Vitamins = Enum('Vitamins', 
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in all_vitamins.items()
        ))

# We now have support for string indexing,
assert(Vitamins.Vitamin_B1 == Vitamins['Vitamin B1'])

# aliases, 
assert(Vitamins.Vitamin_B1 == Vitamins['Thiamine'])

# and alternate spellings
assert(Vitamins.Vitamin_B1 == Vitamins['Thiamin'])

