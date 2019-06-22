recipes = {
    'GCF': 'Green-cuisine frittataa, AT, 2L, p48, 457 cal, 25f, 12c, 47p',
    'PY': 'Power yoghurt, at, 1L, p230, 200 cal, 1.8f, 15.8c, 30p',
    '8LD': '8-layer dinner, PW, 3L, p125, 666 cal, 15.4f, 74.8c, 56.3p',
    'ACB': 'Apple Cinnamon Bar, at, 8S, p 228, 344 cal, 19.1f, 17.9c, 25.1p',
    'CC': 'Classy Chicken, AT, 3L, p124, 470 cal, 18.5f, 19.4c, 56.6p',
    'CBO': 'Chai Blueberry Oatmeal, pW, 2S, p38, 236 cal, 5f, 30.4c, 17.2p',
    'SCP': 'Strawberry Coconut Pudding, at, 1L, p232, 270 cal, 16f, 11.3c, 22.5p',
	'HG': 'Homemade Granola, PW, 5L, p234, 355.2 cal, 21.7f, 32c, 7.9p',
}

remove_last_character = lambda s: s[:-1]

tokenize = lambda recipe: recipe.split(', ')
name = lambda recipe: tokenize(recipe)[0]

calories = lambda recipe: float(tokenize(recipe)[4].split(' ')[0])
meal_scheduling_label = lambda recipe: tokenize(recipe)[1]
servings = lambda recipe: int(remove_last_character(tokenize(recipe)[2]))
fat = lambda recipe: float(remove_last_character(tokenize(recipe)[5]))
carbs = lambda recipe: float(remove_last_character(tokenize(recipe)[6]))
protein = lambda recipe: float(remove_last_character(tokenize(recipe)[7]))

def combine_recipes(name_of_combo, scheduling_label, recipes):
    new_recipe = [name_of_combo]
    number_of_servings = '' # Leave blank while PoC'ing
    page = '' # Leave blank while PoC'ing, refer to all of them later?
    
    new_recipe.append(number_of_servings)
    new_recipe.append(page)

    new_recipe.append(str(sum(map(calories, recipes))))
    new_recipe[-1] += ' cal'

    new_recipe.append(str(sum(map(fat, recipes))))
    new_recipe[-1] += 'f'

    new_recipe.append(str(sum(map(carbs, recipes))))
    new_recipe[-1] += 'c'

    new_recipe.append(str(sum(map(protein, recipes))))
    new_recipe[-1] += 'p'

    return ', '.join(new_recipe)

print(combine_recipes('Strawberry Coconut Pudding with Granola', 'PW', [recipes['SCP'], recipes['HG']]))
    
