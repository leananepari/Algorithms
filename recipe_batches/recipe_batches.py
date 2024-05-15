#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_num_of_batches = math.inf

  for key in recipe:
    if key not in ingredients:
      return 0
    elif ingredients[key] < recipe[key]:
      return 0
    else:
      value = math.floor(ingredients[key] / recipe[key])
      if value < max_num_of_batches:
        max_num_of_batches = value

  return max_num_of_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))