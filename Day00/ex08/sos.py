import sys

alphabet = {'a': 'o-', 'b':'-ooo', 'c':'-o-o', 'd':'-oo', 'e':'o', 'f':'oo-o', 'g':'--o',
                'h':'oooo', 'i':'oo', 'j':'o---', 'k':'-o-', 'l':'o-oo', 'm':'--', 'n':'-o',
                'o':'---', 'p':'o--o', 'q':'--o-', 'r':'o-o', 's':'ooo', 't':'-', 'u':'oo-',
                'v':'ooo-', 'w':'o--', 'x':'-oo-', 'y': '-o--', 'z':'--oo', '0': '-----', '1': 'o----',
                '2': 'oo---', '3': 'ooo--','4': 'oooo-', '5': 'ooooo','6': '-oooo', '7': '--ooo','8':
                '---oo', '9': '----o'}
def encrypte(word):
    morse = ""
    for c in word:
        if (c.isupper()):
            c = c.lower()
        morse += alphabet[c]
        morse += " "
    return morse

print(encrypte(sys.argv[1]))
