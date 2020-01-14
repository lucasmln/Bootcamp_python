import sys
import string

def text_analyzer(text = ""):

    if not text:
        print("What is the text to analyse?")
        text = input()
    print("The text contains " + str(len(text)) + " charachters:")
    print("- " + str(sum(1 for c in text if c.islower())) + " lower letters")
    print("- " + str(sum(1 for c in text if c.isupper())) + " upper letters")
    print("- " + str(sum(1 for c in text if c.isspace())) + " space")
    print("- " + str(sum(1 for c in text if string.punctuation)) + " punctuation marks")
