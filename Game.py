# -- The game class is responsible for all of the game functionality
from main_packages.Board import BoardClass as Board
import random


class Game:
    winner= False
    current = ''

    def __init__(self):
        pass

     # This function handles the main game playing
    @classmethod
    def play_the_game(self):
        global current  # make a variable current as a global to mutate it
        current = 'X'     # the first player is always X
        game_is_running = True
        while(game_is_running):  # This while loop is the soul of the game and will loop to play the game until someone wons
            print(f'\nCurrent Player is: {current}\n')
            flag_tie= False
            if(current == 'O'):
                get_ai = Game.ai()
                if(get_ai < 0):
                    flag_tie=True 
                else:
                    Board.board[get_ai] = current
                    Board.display_board()
                    if(Game.check_win(current)):
                        Game.winner=True
                        break
                    current = Game.change_player(current)
            if(not Game.winner or not flag_tie):
                try:
                    print('Current Player is:  ', current)
                    user_input = int(input('please enter your input 1-9: 😎:   '))-1
                    if(not Game.check_cell(user_input)):  # Handles if the cell is taken already
                        print('\n $$$$ This cell is taken? try an empty one 😅 😅  "-" $$$')
                        Board.display_board()
                        continue
                    if(user_input < 0):  # Handles 0 digit input
                        print(
                                'You must enter one digit from 1--25 only and Zero not Allowed 😟 😟:  !!')
                        Board.display_board()
                        continue
                except Exception as ex:  # Handles exceptions like number out of range, string inputs...etc
                    print('Hey please only numbers between 1-25 🤬 🤬')
                    print(ex)
                    Board.display_board()
                    continue
                Board.board[user_input] = current
                if(Game.check_win(current)):
                    break
                if(Game.check_tie()):
                    print('\nGame is Tie !! Play it again 😫 😫')
                    break
                print('\n')
                Board.display_board()
                current = Game.change_player(current)


              
    @classmethod
    def check_win(self, current):
        if(Game.check_rows(current) or Game.check_diagonal(current) or Game.check_columns(current)):
            # print(Game.check_rows(current))
            # get_mode=
            print(f'{current} has won!!  YaaY 🥳 🥳')
            Board.display_board()
            return True
        return False


    # This function handles changing player
    @classmethod
    def change_player(self, current):
        if(current == 'X'):
            current = 'O'
            return current
        else:
            current = 'X'
            return current

    # This function handles a row wining

    @classmethod
    def check_rows(self, current):
        if(Board.board[0] == current and Board.board[1] == current and Board.board[2] == current and Board.board[3] == current and Board.board[4] == current):
            return True
        elif (Board.board[5] == current and Board.board[6] == current and Board.board[7] == current and Board.board[8] == current and Board.board[9] == current):
            return True
        elif (Board.board[10] == current and Board.board[11] == current and Board.board[12] == current and Board.board[13] == current and Board.board[14] == current):
            return True
        elif (Board.board[15] == current and Board.board[16] == current and Board.board[17] == current and Board.board[18] == current and Board.board[19] == current):
            return True
        elif (Board.board[20] == current and Board.board[21] == current and Board.board[22] == current and Board.board[23] == current and Board.board[24] == current):
            return True
        return False

    # This function handles a columns wining

    @classmethod
    def check_columns(self, current):
        if(Board.board[0] == current and Board.board[5] == current and Board.board[10] == current and Board.board[15] == current and Board.board[20] == current):
            return True
        elif (Board.board[1] == current and Board.board[6] == current and Board.board[11] == current and Board.board[16] == current and Board.board[21] == current):
            return True
        elif (Board.board[2] == current and Board.board[7] == current and Board.board[12] == current and Board.board[17] == current and Board.board[22] == current):
            return True
        elif (Board.board[3] == current and Board.board[8] == current and Board.board[13] == current and Board.board[18] == current and Board.board[23] == current):
            return True
        elif (Board.board[4] == current and Board.board[9] == current and Board.board[14] == current and Board.board[19] == current and Board.board[24] == current):
            return True
        return False

    # This function handles a diagonal winning
    @classmethod
    def check_diagonal(self, current):
        if(Board.board[0] == current and Board.board[6] == current  and Board.board[12] == current and Board.board[18] == current and Board.board[24] == current):
            return True
        elif (Board.board[4] == current and Board.board[8] == current and Board.board[12] == current and Board.board[16] == current and Board.board[20] == current):
            return True

 # This function handles a tie in the game
    @classmethod
    def check_tie(self):
        if('_' not in Board.board):
            return True

    # This function checks each cell if its taken or not
    @classmethod
    def check_cell(self, value):
        if Board.board[value] == '_':
            return True

    #! NOT WORKING YET.. RIP 💀
    @classmethod
    def mini_max(self, board, depth, isMaximizingPlayer):
        return True

    # A method to handle the AI player
    @classmethod
    def ai(self):
        while(True):
            num = Game.get_new_random()
            if(Game.check_cell(num)):
                return num
            else:
                if(Game.check_tie()):
                    return 0
                continue

    # Generates randome number for tha AI player
    @classmethod
    def get_new_random(self):
        return random.randint(0,24)