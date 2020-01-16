class GotCharacter:
    def __init__(self, name, is_alive):
        self.first_name = name
        self.is_alive = is_alive

class Stark(GotCharacter):
    '''A class representing the Stark family. Or when bad things happen to good
people.'''
    def __init__(self, name = None, is_alive = True):
        super().__init__(name = name, is_alive = is_alive)
        self.familly_name = "Stark"
        self.house_word = "Winter is comming"

    def print_house_words(self):
        print(self.house_word)

    def die(self):
        self.is_alive = False
