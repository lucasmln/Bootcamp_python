import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, last, create, lst):
        self.name = name
        self.last_uptdate = last
        self.creation_date = create
        self.recipe_list = lst

    def get_recipe_by_name(self, name):
        for recipe in self.recipe_list['starter']:
            if recipe.name == name:
                print(recipe)
        for recipe in self.recipe_list['lunch']:
            if recipe.name == name:
                print(recipe)
        for recipe in self.recipe_list['dessert']:
            if recipe.name == name:
                print(recipe)
        pass

    def get_all_recipes_by_type(self, recipe_type):
        if  (recipe_type == 'lunch' or recipe_type == 'dessert' or recipe_type == 'starter'):
            for cle in self.recipe_list[recipe_type]:
                print "%s :" % recipe_type, cle.name
        pass

    def add_recipe(self, recipe):
        if  (recipe.recipe_type == 'lunch' or recipe.recipe_type == 'dessert'
            or recipe.recipe_type == 'starter'):
            self.recipe_list[recipe.recipe_type].append(recipe)
            self.last_uptdate = datetime.datetime.now()
        else:
            pass
        pass
