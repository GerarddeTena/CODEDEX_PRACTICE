# Let's create the fantastic ROCK PAPER SCISSORS LIZARD SPOCK game using OOP to practice some skills::
import random

def game_interface():
    equal = '========================================================\n'
    title = '                    GAME RPSLS V2                       \n'
    obj_description = '                  AVAILABLE OBJECTS:                    \n'
    objects = '0) Rock\n 1) Paper\n 2) Scissors\n 3) Lizard\n 4) Spock\n'
    line = '-----------------------------------------------------\n'
    print(equal, title, line, obj_description, line, objects, line)

def play_again():
    while True:
        again = input('Play again? (y/n): ')
        if again.lower() == 'y':
            return True
        elif again.lower() == 'n':
            return False
        else:
            print('Please enter y or n')

"""
First, we will create the input player_name and store it in the Player class constructor.
"""
class Player:
    def player(self):
        self.player_name = input('Enter your name: ')
# After the input is stored, we will add conditional statements in a while loop to validate the entries and make the process more interesting.
        while True:
            if self.player_name != '' and not self.player_name.isdigit():
                break
            else:
                print('Please, introduce a valid name!')
                self.player_name = input('Enter your name: ')
# This loop allows the player to enter a valid name, ensuring it is not a digit or an empty string.
# Next, we will create the game options and the NPC.
class Options(Player):
    def options(self):
        self.player()
# We have created a new class that inherits the methods from the parent class. This is called inheritance.
        self.game_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.computer = random.randint(0, 4)
        while True:
            self.player_choice = int(input(f'Choose an option by its value: {list(enumerate(self.game_options))}'))
            if self.player_choice > 4 or self.player_choice < 0:
                print('Choose a number between 0 and 4 please... not so difficult right? -_- ...')
                self.player_choice = int(input(f'Choose an option by its value: {list(enumerate(self.game_options))}'))
            else:
                break
# In the previous class, we created the options to choose from. Next, to allow us to use an int(input()) to select an option from an array of strings, we need to use the list(enumerate()) method which allows us to
# access to the index (0 to 4).
class Winnings(Options):
    def wins(self):
        self.options()
        self.wins_at = {
            'Rock':['Lizard', 'Scissors'], 
            'Paper':['Rock', 'Spock'], 
            'Scissors':['Paper', 'Lizard'], 
            'Lizard':['Paper', 'Spock'], 
            'Spock':['Rock', 'Scissors']
        }
        print(f'{self.player_name} choose: {self.game_options[self.player_choice]}\nComputer choose: {self.game_options[self.computer]}\n')
# We've established the game rules in a dictionary that defines what beats what.     
class Conditions(Winnings):
    def conditions(self):
        self.wins()
        player_option = self.game_options[self.player_choice]
        computer_option = self.game_options[self.computer]
        if player_option == computer_option:
            return 'Tie'
        elif computer_option in self.wins_at[player_option]:
            return 'Player'
        else:
            return 'Computer'
# To avoid hardcoding the project, we've set the game-winning conditions in a single class to have better control and manage potential errors.
# Now we'll store the scores to track how many games each player wins
class Results(Conditions):
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
    def result(self):
        result = self.conditions()
        if result == 'Tie':
            print('Clear tie!!')
        elif result == 'Player':
            print(f'{self.player_name} wins!!')
            self.player_score += 1
        else:
            print('Computer wins!!')
            self.computer_score += 1
# Let's create a class that differentiates each player and their points.
class Table_Score(Results):
    def scores(self):
        self.result()
        print(f'{self.player_name} has: {self.player_score} points.\n Computer has {self.computer_score} points')
# Lastly, we'll instantiate the last class to start the game. Next, we'll create a loop that calls a function we've declared to ask if we want to play again or not.
class GamePlay(Table_Score):
    def __init__(self):
        self.game_play = Table_Score()
    def game_init(self):
# # Bonus: We can create a game interface to make more prettier our game.
        game_interface()
        while True:
            self.game_play.scores()
            if not play_again():
                break
game_session = GamePlay()
game_session.game_init()
