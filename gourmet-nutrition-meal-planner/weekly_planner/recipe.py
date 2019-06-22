recipes = {
    'GCF': 'Green-cuisine frittataa, AT, 2L, p48, 457 cal, 25f, 12c, 47p',
    'PY': 'Power yoghurt, at, 1L, p230, 200 cal, 1.8f, 15.8c, 30p',
    '8LD': '8-layer dinner, PW, 3L, p125, 666 cal, 15.4f, 74.8c, 56.3p',
    'ACB': 'Apple Cinnamon Bar, at, 8S, p 228, 344 cal, 19.1f, 17.9c, 25.1p',
    'CC': 'Classy Chicken, AT, 3L, p124, 470 cal, 18.5f, 19.4c, 56.6p',
    'CBO': 'Chai Blueberry Oatmeal, pW, 2S, p38, 236 cal, 5f, 30.4c, 17.2p',
    'SCP': 'Strawberry Coconut Pudding, at, 1L, p232, 270 cal, 16f, 11.3c, 22.5p',
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
