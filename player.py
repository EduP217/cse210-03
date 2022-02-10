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
        self._guessed_letters_list = []

    def ask_the_player(self):
        """Ask the player for a guessed letter.
        
        Args:
            self (Player): An instance of Player.
        """
        ask_letter = input('Guess a letter [a-z]: ')
        self._guessed_letter.append(ask_letter)
        
    
    def get_guessed_letters(self, word_selected):
        """Clear the selected word of any spaces.
        Print the correct guessed letters entered by
        the pLayer based on the random selected word.
        
        Args:
            self (Player): An instance of Player.
            word_selected (string): The random selected word for the player to guess.
        """
        guessed_letters = ''
        clean_word_selected = word_selected.strip()
        for letter in clean_word_selected:
            if letter in self._guessed_letters_list:
                guessed_letters += letter
            else:
                guessed_letters += '_'
        print(guessed_letters)


