import sys
import string

if (len(sys.argv) > 3):
    print("Too many argument.")
    exit(0)
elif (len(sys.argv) < 3):
    print("Not enought argument")
    exit(0)
elif not sys.argv[1].isdigit():
    exit(0)
    print("only numbers")
elif not sys.argv[2].isdigit():
    print("only numbers")
    exit(0)
print("Sum : \t\t", int(sys.argv[1]) + int(sys.argv[2]))
print("Difference :\t\t", int(sys.argv[1]) - int(sys.argv[2]))
print("Product :\t\t", int(sys.argv[1]) * int(sys.argv[2]))
print("Quotient :\t\t", float(sys.argv[1]) / float(sys.argv[2]) if float(sys.argv[2]) != 0 else "ERROR (div by zero)")
print("Remainder :\t\t", float(sys.argv[1]) % float(sys.argv[2]) if float(sys.argv[2]) != 0 else "ERROR (modulo by zero)")
