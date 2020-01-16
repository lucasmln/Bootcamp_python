class Recipe:
    def __init__(self, name, lvl, time, ingredient, descri, recipe_type):
        self.name = name
        self.cooking_level = lvl
        self.cooking_time = time
        self.ingredient = ingredient
        self.description = descri
        self.recipe_type = recipe_type

    def __str__(self):
        txt = ""
        txt += "Name : %s\n" % self.name
        txt += "Cooking_level : %d\n" % self.cooking_level
        txt += "Cooking time : %d\n" % self.cooking_time
        txt += "Ingredient : %s\n" % self.ingredient
        txt += "Description : %s\n" % self.description
        txt += "Recipe type : %s" % self.recipe_type
        return txt
