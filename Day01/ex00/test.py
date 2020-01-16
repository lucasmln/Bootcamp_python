from book import Book
from recipe import Recipe
import datetime

bolo = Recipe("bolognaise", 2, 15, ["pate", "viande", "sauce"], "c'est bon", "lunch")
cookie = Recipe("cookie", 1, 20, ["pate", "pepite de choco", "beurre"], "succulent", "dessert")
salad = Recipe("salad", 3, 15, ["salad", "tomate", "oeuf", "huile", "vinaigre"], "", "starter")

lst = {'starter' : [], 'lunch' : [], 'dessert' : []}

cookbook = Book("cookbook", datetime.datetime.now(), datetime.datetime.now(), lst)
cookbook.add_recipe(bolo)
cookbook.add_recipe(cookie)
cookbook.add_recipe(salad)

cookbook.get_all_recipes_by_type('lunch')
cookbook.get_all_recipes_by_type('dessert')
cookbook.get_all_recipes_by_type('starter')

cookbook.get_recipe_by_name("cookie")
