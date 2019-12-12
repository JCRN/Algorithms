#!/usr/bin/python


# 1. Key match:
#        - for i in recipe i also in ingredients
# 2. Verify there are enough ingredients:
#        - for i in recipe ingredients[i] >= recipe[i]
# 3. Determine how many batches can be made:
#        - smallest quotient derived from ingredients[i] / recipe[i]

import math


def recipe_batches(recipe, ingredients):
    batches = []
    nope = 'Not enough ingredients to make this recipe'
    for i in recipe:
        if i in ingredients:
            if ingredients[i] / recipe[i] >= 1:
                batches.append(math.floor(ingredients[i] / recipe[i]))
            else:
                return print(nope)
        else:
            return print(nope)
    return print(f'{min(batches)} can be made with the available ingredients.')


recipe_batches({'milk': 100, 'butter': 50, 'flour': 5}, {'milk': 132, 'butter': 48, 'flour': 51})

recipe_batches({'milk': 100, 'butter': 50, 'flour': 5}, {'milk': 332, 'butter': 200, 'flour': 51})


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
