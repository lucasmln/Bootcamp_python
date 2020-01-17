import random

def generator(text, sep = " ", option = None):
    if not isinstance(text, str):
        print("ERROR")
    else:
        res = text.split(sep)
    if option == "ordered":
        res.sort()
    elif option == "unique":
        res = set(res)
        res = (list(res))
    elif option == "shuffle": 
        random.shuffle(res)
    else:
        print("ERROR")
        return
    return (res)
