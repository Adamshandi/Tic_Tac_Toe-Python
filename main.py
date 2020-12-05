### -@Author: Adam Shandi, City University of Seattle
### - This is the main file where the game is started
### - ! Please run on terminal with --> python/python3 main.py
### -
from main_packages.Board import BoardClass as Board
from main_packages.Game import Game as Game



if __name__ == "__main__":
    board = Board()                ## instantiate the board 
    # board.initialize_board()      ## initialize the board
    board.display_board()         ## Display the board

    ##! Game Starts here
    Game.play_the_game()




    ########! Clark Feedback !#########
# our check_columns method has a parameter of slef.

# if your method is returning a boolean value, use names such as has_winner, is_complete, has_tie.

# Check this out: https://dev.to/michi/tips-on-naming-boolean-variables-cleaner-code-35ig

# Instead of having a initialize_board method. use the __init__ to initialize the board.

# Also, in the user prompt, mention if it is Player 1 and Player 2. 
