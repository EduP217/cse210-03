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
        """
        Init method : Construct a new instance of the class
        """
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
        """
        Random select word method : select one item of the word list and set into a private attribute.
        """
        self.__word_selected = random.choice(self.__words_list)
    
    def get_words_list(self):
        """
        Get words list method : return the private word list value.
        """
        return self.__words_list
    
    def get_word_selected(self):
        """
        Get word selected : return the private word selected randomly.
        """
        return self.__word_selected.lower()
    
    def get_word_selected_length(self):
        """
        Get word selected length : return the word length of the private attribute.
        """
        letters = []
        for letter in self.__word_selected:
            if letter != ' ':
                letters.append(letter)
        
        return len(letters)