# The class is responsible for the board in the game
class BoardClass:
    board = []

    # An empty constructor
    # might needed to check and test the board array
    def __init__(self):
        BoardClass.board = [
            '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_'

        ]

    # Method fo initialize an empty board 3 X 3

    def initialize_board(self):
        pass
        # BoardClass.board = [
        #     '_', '_', '_', '_', '_',
        #     '_', '_', '_', '_', '_',
        #     '_', '_', '_', '_', '_',
        #     '_', '_', '_', '_', '_',
        #     '_', '_', '_', '_', '_'

        # ]

    # a class method to draw the board.

    @classmethod
    def display_board(self):
        print(' | ' + BoardClass.board[0] + ' | ' + BoardClass.board[1] + ' | ' +
              BoardClass.board[2] + ' | ' + BoardClass.board[3] + ' | ' + BoardClass.board[4] + ' | ')
        print(' | ' + BoardClass.board[5] + ' | ' + BoardClass.board[6] + ' | ' +
              BoardClass.board[7] + ' | ' + BoardClass.board[8] + ' | ' + BoardClass.board[9] + ' | ')
        print(' | ' + BoardClass.board[10] + ' | ' + BoardClass.board[11] + ' | ' +
              BoardClass.board[12] + ' | ' + BoardClass.board[13] + ' | ' + BoardClass.board[14] + ' | ')
        print(' | ' + BoardClass.board[15] + ' | ' + BoardClass.board[16] + ' | ' +
              BoardClass.board[17] + ' | ' + BoardClass.board[18] + ' | ' + BoardClass.board[19] + ' | ')
        print(' | ' + BoardClass.board[20] + ' | ' + BoardClass.board[21] + ' | ' +
              BoardClass.board[22] + ' | ' + BoardClass.board[23] + ' | ' + BoardClass.board[24] + ' | ')
