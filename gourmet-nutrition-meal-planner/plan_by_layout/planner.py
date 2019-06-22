from recipe import meal_scheduling_label, name, calories, fat, carbs, protein, recipes

def plan_day(daily_meal_layout, recipes):
    # A daily meal layout is on the form
    # monday = ['AT', 'at', 'PW', 'at', 'AT']
    # wednesday = ['AT', 'pW', 'PW', 'AT', 'AT']
    daily_meal_plan = []
    _recipes = recipes.copy()

    for scheduling_label in daily_meal_layout:
        # Use keys here instead of items to in-place edit the dictionary
        for recipe_label in list(_recipes.keys()):
           if meal_scheduling_label(_recipes[recipe_label]) == scheduling_label:
               daily_meal_plan.append((recipe_label, scheduling_label))
               del _recipes[recipe_label]
               break

    return daily_meal_plan

def aggregate_calories(recipes):
    return list(map(calories, recipes))

def aggregate_fats(recipes):
    return list(map(fat, recipes))

def aggregate_carbs(recipes):
    return list(map(carbs, recipes))

def aggregate_proteins(recipes):
    return list(map(protein, recipes))

def pretty_print_day(day_name, daily_meal_plan, recipes):
    # A daily meal plan is on the form 
    # monday = [('GCF', 'AT'), ('PY', 'at'), ('8LD', 'pW'), ('ACB', 'at'), ('CC', 'AT')]
    def get_recipes(daily_meal_plan, recipes):
        return [recipes[recipe_label] for (recipe_label, _) in daily_meal_plan]

    recipes = get_recipes(daily_meal_plan, recipes)

    cals = aggregate_calories(recipes)
    f = aggregate_fats(recipes)
    c = aggregate_carbs(recipes)
    p = aggregate_proteins(recipes)
    
    print(day_name)
    print('===')
    print(f'{list(map(lambda s: s.title(), map(name, recipes)))}')
    print(f'Calories: {sum(cals)}')
    print(f'Fat: {f}. Total={sum(f)}')
    print(f'Carbs: {c}. Total={sum(c)}')
    print(f'Protein: {p}. Total={sum(p)}')

monday_layout = ['AT', 'at', 'PW', 'at', 'AT']
monday_meal_plan = plan_day(monday_layout, recipes)
pretty_print_day('Monday', monday_meal_plan, recipes)
print('')
wednesday_layout = ['AT', 'pW', 'PW', 'at', 'AT']
wednesday_meal_plan = plan_day(wednesday_layout, recipes)
pretty_print_day('Wednesday', wednesday_meal_plan, recipes)

