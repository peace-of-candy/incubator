recipes = {
    'GCF': 'Green-cuisine frittataa, AT, 2L, p48, 457 cal, 25f, 12c, 47p',
    'PY': 'Power yoghurt, at, 1L, p230, 200 cal, 1.8f, 15.8c, 30p',
    '8LD': '8-layer dinner, PW, 3L, p125, 666 cal, 15.4f, 74.8c, 56.3p',
    'ACB': 'Apple Cinnamon Bar, at, 8S, p 228, 344 cal, 19.1f, 17.9c, 25.1p',
    'CC': 'Classy Chicken, AT, 3L, p124, 470 cal, 18.5f, 19.4c, 56.6p',
    'CBO': 'Chai Blueberry Oatmeal, pW, 2S, p38, 236 cal, 5f, 30.4c, 17.2p',
    'SCP': 'Strawberry Coconut Pudding, at, 1L, p232, 270 cal, 16f, 11.3c, 22.5p',
}

def tokenize(recipe):
    return recipe.split(', ')

def name(recipe):
    return tokenize(recipe)[0]

def meal_scheduling_label(recipe):
    # AT: Anytime meal
    # at: Anytime snack
    # PW: Post-workout meal/snack
    # pW: Pre-workout meal/snack
    return tokenize(recipe)[1]

def calories(recipe):
    return float(tokenize(recipe)[4].split(' ')[0])

def convert_macro_to_float(macro_label):
    def macro_extractor_decorator(func):
        def func_wrapper(recipe):
            return float(func(recipe).replace(macro_label, ''))

        return func_wrapper

    return macro_extractor_decorator

@convert_macro_to_float('f')
def fat(recipe):
    return tokenize(recipe)[5]

@convert_macro_to_float('c')
def carbs(recipe):
    return tokenize(recipe)[6]

@convert_macro_to_float('p')
def protein(recipe):
    return tokenize(recipe)[7]
