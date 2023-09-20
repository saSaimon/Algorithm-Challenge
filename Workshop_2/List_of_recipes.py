recipes = [["yeast", "flour"], ["bread", "meat"], ["flour", "meat"]]
ingredients = ["yeast", "flour", "meat"]

def find_recipes_you_can_make(recipes, available_ingredients):
    recipes_you_can_make = []

    for recipe in recipes:
        if all(ingredient in available_ingredients for ingredient in recipe):
            recipes_you_can_make.append(recipe)

    return recipes_you_can_make



print("Recipes you can make:")
print(find_recipes_you_can_make(recipes, ingredients))

def find_best_recipe(recipes, available_ingredients):
    best_recipe = None
    most_ingredients_used = 0

    for recipe in recipes:

        ingredients_used = 0
        for ingredient in recipe:
            if ingredient in available_ingredients:
                ingredients_used += 1

        if ingredients_used > most_ingredients_used:
            most_ingredients_used = ingredients_used
            best_recipe = recipe

    return best_recipe



print("Best recipe:", find_best_recipe(recipes, ingredients))

def find_missing_ingredients(recipes, available_ingredients):
    missing_ingredients = set()

    for recipe in recipes:
        for ingredient in recipe:
            if ingredient not in available_ingredients:
                missing_ingredients.add(ingredient)

    return list(missing_ingredients)

print("Missing ingredients for all recipes:")
print(find_missing_ingredients(recipes, ingredients))

