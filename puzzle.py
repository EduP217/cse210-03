import random
"""
class Puzzle
"""
class Puzzle:
    """
    Class Puzzle
    Attributes: _words_list (array) = static list of words to guess
                _word_selected (string) = the word that holds a randomly word selected from list
    """
    
    def __init__(self):
        self.__words_list = [
            "peel",
            "Lawnmower",
            "Summer",
            "Whisk",
            "Cupcake",
            "Sleeping Vegas",
            "Train bed",
            "Boardgame",
            "Beehive",
            "Lemon",
            "Wreath",
            "Waffles",
            "Bubble",
            "Whistle",
            "Snowball",
            "Bouquet",
            "Headphones",
            "Fireworks",
            "Igloo",
            "Ferris bag",
            "Bruise",
            "Fog",
            "Crust",
            "Battery",
            "Paris",
            "Beach",
            "Mountains",
            "Hawaii",
            "Mount World",
            "Mexico",
            "Giraffe",
            "Koala",
            "Wasp",
            "Scorpion",
            "Lion",
            "Salamander",
            "Dolphin",
            "Frog",
            "Panda",
            "Platypus",
            "T-rex",
            "Meerkat",
            "Eagle Pole",
            "Farm",
            "Disney Rushmore",
            "USA",
            "Hospital",
            "Attic",
            "Japan",
            "Library",
            "Desert",
            "Mars",
            "Washington wheel",
            "Banana Strawberry",
            "Eclipse",
            "Chandelier",
            "Ketchup",
            "Toothpaste",
            "Rainbow",
            "Bunk station",
            "North DC",
        ]
        self.__word_selected = ""
    
    def random_select_word(self):
        self.__word_selected = random.choice(self.__words_list)
    
    def get_words_list(self):
        return self.__words_list
    
    def get_word_selected(self):
        return self.__word_selected
    
    def get_word_selected_length(self):
        return len(self.__word_selected)