import sys

if (len(sys.argv) != 2):
    print("ERROR")
    exit()
nb = 0
for lettre in sys.argv[1]:
    if not lettre.isdigit():
        print("ERROR")
        exit()
    nb = nb * 10 + int(lettre)
if (nb == 0):
    print("I'm Zero.")
elif (nb % 2 == 0):
    print("I'm Even.")
elif (nb % 2 == 1):
    print("I'm Odd.")
