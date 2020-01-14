import sys

k = 1
rev = ""

while 0 < len(sys.argv) - k:
    s = sys.argv[len(sys.argv) - k]
    for lettre in reversed(s):
        if lettre.isupper():
            rev += lettre.lower()
        elif lettre.islower():
            rev += lettre.upper()
        else:
            rev += lettre
    if len(sys.argv) - k > 1:
        rev += " "
    k += 1
if len(sys.argv) > 1:
    print(rev)
