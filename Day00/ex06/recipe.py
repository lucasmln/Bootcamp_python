def print_recipe(recipe):
    for key in cookbook.keys():
        if key == recipe:
            print ("Recipe for", recipe + " :\nIngredients list :", cookbook[recipe], "\nTakes", cookbook["time"][recipe], "minutes of cooking")

def del_recipe(recipe):
    for key in cookbook.keys():
        if key == recipe:
            cookbook.pop(recipe)
            cookbook["time"].pop(recipe)
            cookbook["type"].pop(recipe)

def print_cookbook():
    for recipe in cookbook.keys():
        try:
            print ("Recipe for", recipe + " :\nIngredients list :", cookbook[recipe], "\nTakes", cookbook["time"][recipe], "minutes of cooking\n")
        except KeyError:
            pass

def add_recipe(recipe, ingredients, meal_type, prep_time):
    tmp = ingredients.split(" ")
    cookbook[recipe] = tmp
    cookbook["time"][recipe] = prep_time
    cookbook["type"][recipe] = meal_type

sandwich, cake, salad = ("ham", "bread", "cheese", "tomatoes"), ("flour", "sugar", "eggs"), ("avocado", "arugula", "tomatoes", "spinach")
time = {}
type_meal = {}
time["sandwich"], time["cake"], time["salad"], type_meal["salad"], type_meal["cake"], type_meal["sandwich"] = 10, 60, 15, "lunch", "dessert", "lunch"
cookbook = {}
cookbook["sandwich"], cookbook["cake"], cookbook["salad"], cookbook["time"], cookbook["type"] = sandwich, cake, salad, time, type_meal
x = 0
while x != '5':
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    x = input()
    if x > '9' or x < '1':
        print("This option does not exist, please type the corresponding number. To exit, enter 5")
    elif x == '1':
        add_recipe(input("Enter the name of the recipe\n"), input("Enter ingredients\n"), input("Enter type meal\n"), input("Enter time prep\n"))
    elif x == '2':
        del_recipe(input("Enter the name of the recipe\n"))
    elif x == '3':
        print_recipe(input("Enter the name of the recipe\n"))
    elif x == '4':
        print_cookbook()
    print("\n")
print ("cookbook closed")
exit()
