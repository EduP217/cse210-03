# cse210-03
Jumper Game

# Jumper Specification
## Description
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Rules
Jumper is played according to the following rules.

* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* If the puzzle is solved the game is over.
* If the player has no more parachute the game is over.

## Required Technologies
---
* Python 3.8.0
---

# Team members - Thursday 5PM (MST)
 Names and email addresses
* Yurinii Fuentes  fue21007@byui.edu 
* Eduardo Prieto  pri21002@byui.edu
* Oscar Candia  davidcandianeg@gmail.com

## Project Structure
---
The project is organized as follows:
```
root                    (project root folder)
+-- parachute.py        (specific class)
+-- player.py           (specific class)
+-- puzzle.py           (specific class)
+-- game.py             (specific class)
+-- __main__.py         (program entry point)
+-- README.md           (general info)
```

# Project Design
* Parachute class
    -   This class initialize the parachute string
             ___
            /___\
            \   /
             \ /
              o x
    -   This class initialize the status of the parachute
        status = [alive, dead]
    -   This class has functions that return the value of the variables
    -   This class has a function to check the parachute and change the status value
        - if the status is dead, change the parachute from 'o' to 'x'

* Player class
    -   This class initialize the letter guessed
        guessed = []
        guessed = ['c', 'a', 'b']
    
    -   This class has a function to ask the player for a letter

* Puzzle class
    -   This class initialize the static list of words
    -   This class initialize the random word selected
    -   This class has functions that return the value of the variables
    -   This class has a function to make a random selection for the word of the list

* Game class
    -   This class initialize the guessed variable [True, False]
    -   This class initialize an object of Player
    -   This class initialize an object of Puzzle
    -   This class initialize an object of Parachute
    -   This class has the function starts
        -   In this function, print the parachute string
        -   In this function, invoke the function to ask the player.
        -   In this function, print the spaces of the word.
        -   In this function, print the parachute string
        -   In this function, validates the parachute status
        -   If parachute is 'dead' end process
        -   else, validates the word guessed, if it's true game ends.
    
    - This class has the function validate_word_guessed