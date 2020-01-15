import sys

if len(sys.argv) != 3 or sys.argv[2] > '9' or sys.argv[2] < '0':
    print("ERROR")
    exit()
lst = sys.argv[1].split()
i = 0
while i < len(lst):
    if len(lst[i]) < int(sys.argv[2]):
        del lst[i]
    else:
        i += 1
print(lst)
