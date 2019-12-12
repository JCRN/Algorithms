#!/usr/bin/python


# 1. Key match:
#        - for i in recipe i also in ingredients
# 2. Verify there are enough ingredients:
#        - for i in recipe ingredients[i] >= recipe[i]
# 3. Determine how many batches can be made:
#        - smallest quotient derived from ingredients[i] / recipe[i]

import math


def recipe_batches(recipe, ingredients):
    batched = []
    for i in recipe:
        if i in ingredients:
            if ingredients[i] / recipe[i] >= 1:
                batched.append(math.floor(ingredients[i] / recipe[i]))
            else:
                return 0
        else:
            return 0
    return min(batched)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
