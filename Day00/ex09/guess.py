import random

nb_secret = random.randint(1, 99)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck")

nb = 100
cmpt = 0
while int(nb) != nb_secret or nb == "exit":
    nb = input("What's yout guess between 1 and 99\n")
    if nb == "exit":
        print("Goodbye!")
        exit()
    if not nb.isdigit():
        print("That's not a number.")
    elif int(nb) < nb_secret:
        print("Too low!")
    elif int(nb) > nb_secret:
        print("Too high")
    elif int(nb) == nb_secret:
        break
    cmpt += 1
if nb_secret == 42:
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if cmpt + 1 == 1:
    print("Congratulations, you've got it on your first try!")
    print("You won in", cmpt + 1, "attempts!")
else:
    print("Congratulations, you've got it!")
