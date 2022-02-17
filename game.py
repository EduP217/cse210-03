from puzzle import Puzzle
from parachute import Parachute
from player import Player

"""
class Game
"""
class Game:
    
    def __init__(self):
        self.__is_running = True
        self.__puzzle = Puzzle()
        self.__player = Player()
        self.__parachute = Parachute()
        
    def starts(self):
        self.__puzzle.random_select_word()
        puzzle_word = self.__puzzle.get_word_selected()
        
        self.__player.get_guessed_letters(puzzle_word)
        self.__parachute.print_parachute_graph()
        
        while self.__is_running:
            is_letter_in_word = self.__player.ask_the_player(puzzle_word)
            self.__player.get_guessed_letters(puzzle_word)
            self.__parachute.update_parachute_info(is_letter_in_word)
            parachute_status = self.__parachute.get_parachute_status()
            
            if parachute_status:
                if self.validate_word_selected_versus_letters_guessed(self.__puzzle.get_word_selected_letters(), self.__player.get_list_letters_guessed()):
                    print(f'Excellent! word was guessed, your player is {self.__parachute.get_parachute_status_message()}.')
                    self.__is_running = False
            else:
                print(f'Sorry! word missed, your player is {self.__parachute.get_parachute_status_message()}.')
                self.__is_running = False
    
    def validate_word_selected_versus_letters_guessed(self, word_selected_letters, list_letters_guessed):
        word_guessed = False
        
        for letter in word_selected_letters:
            if letter.lower() not in list_letters_guessed:
                word_guessed = False
                return False
            else:
                word_guessed = True
        
        return word_guessed