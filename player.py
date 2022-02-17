class Player:
    """The letters guessed by the player.
        
    The responsability of Player is to ask the player for a letter to guess the puzzle word.

    Attributes:
        guessed_letter (list[string]): Letter guessed by the player.
        .........promp (string) The prompt to the player.......
    """
    
    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): An instance of Player.
        """
        self.__guessed_letters_list = []

    def ask_the_player(self, word_selected):
        """Ask the player for a guessed letter.
        
        Args:
            self (Player): An instance of Player.
        """
        ask_letter = input('Guess a letter [a-z]: ').lower()
        
        if ask_letter == ' ':
            print('WARNING - character not allowed.')
            return True
        
        if ask_letter in word_selected:
            if ask_letter not in self.__guessed_letters_list:
                self.__guessed_letters_list.append(ask_letter)
            return True
        
        return False
    
    def get_guessed_letters(self, word_selected):
        """Print the correct guessed letters entered by
        the pLayer based on the random selected word.
        
        Args:
            self (Player): An instance of Player.
            word_selected (string): The random selected word for the player to guess.
        """
        guessed_letters = ''
        for letter in word_selected:
            if letter == ' ':
                guessed_letters += letter
            else:
                if letter in self.__guessed_letters_list:
                    guessed_letters += letter
                else:
                    guessed_letters += '_'
            
            guessed_letters += ' '
        print(guessed_letters)
    
    def get_list_letters_guessed(self):
        return self.__guessed_letters_list


