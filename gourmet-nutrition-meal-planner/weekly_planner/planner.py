from recipe import meal_scheduling_label, name, calories, fat, carbs, protein, recipes, servings

def plan_days(daily_meal_layouts, recipes):
    daily_meal_plans = []

    _recipes = {recipe_label: servings(recipe)*[recipe] for recipe_label, recipe in recipes.items()}

    for daily_meal_layout in daily_meal_layouts:
        daily_meal_plan = []

        for scheduling_label in daily_meal_layout:
            # Use keys here instead of items to in-place edit the dictionary
            for recipe_label in list(_recipes.keys()):
                if len(_recipes[recipe_label]) == 0:
                    continue

                if meal_scheduling_label(_recipes[recipe_label][0]) == scheduling_label:
                    tup = (recipe_label, scheduling_label)
                    if tup not in daily_meal_plan: # Don't reuse a recipe twice in a day
                        daily_meal_plan.append((recipe_label, scheduling_label))
                        _recipes[recipe_label].pop()
                        break

        daily_meal_plans.append(daily_meal_plan)

    return daily_meal_plans

def aggregate_calories(recipes):
    return list(map(calories, recipes))

def aggregate_fats(recipes):
    return list(map(fat, recipes))

def aggregate_carbs(recipes):
    return list(map(carbs, recipes))

def aggregate_proteins(recipes):
    return list(map(protein, recipes))

def pretty_print_day(day_name, daily_meal_plan, recipes):
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
tuesday_layout = ['AT', 'at', 'AT', 'pW', 'AT']
wednesday_layout = ['AT', 'pW', 'PW', 'at', 'AT']
thursday_layout = ['AT', 'at', 'AT', 'at', 'AT']
friday_layout = ['AT', 'at', 'PW', 'at', 'AT']

print(plan_days([monday_layout, wednesday_layout], recipes))
