import random
import math


class Game:
    # Initialising
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.winner = None
        self.turn = 'X'
        self.isContinue = True
        self.canMove = [i for i in range(1, 10)]


    # start the game from here
    def play(self, playerMode):

        self.displayBoard()

        while self.isContinue:
            if playerMode == '1':
                self.computerMove()
            elif playerMode == '2':
                self.makeMove()
            self.isOver()
            self.isTie()

        if self.winner != None:
            print('==================')
            print('| ' + self.winner + ' PLAYER WON!! |')
            print('==================')
        else:
            print('=================')
            print('| GAME IS TIE!! |')
            print('=================')


    # Displays the board in tic tac toe format
    def displayBoard(self):
        print(self.board[0], '|', self.board[1], '|', self.board[2])
        print('----------')
        print(self.board[3], '|', self.board[4], '|', self.board[5])
        print('----------')
        print(self.board[6], '|', self.board[7], '|', self.board[8])


    # Make moves by player and computer also, for single player game
    def computerMove(self):

        print()

        if self.turn == 'X':
            print(self.turn + "'s Player Turn")
            pos = input('Choose a position from 1 to 9: ')
            try:
                pos = int(pos)
            except:
                print('Please enter a valid position')     

        else:
            print("Computer's move")
            pos = self.computer()

        if pos <= 9 and self.isValid(pos-1):
            self.board[pos-1] = self.turn
            del self.canMove[self.canMove.index(pos)]
            self.turn = 'X' if self.turn == 'O' else 'O'
            self.displayBoard()
            
        else:
            print('=================================')
            print('| Please enter a valid position |')
            print('=================================')    


    # Computer chooses a place according to valid spaces
    def computer(self):
        pos = random.choice(self.canMove)
        return pos


    # function to make move by player, for multiplayer game
    def makeMove(self):
        # print('____________________________')
        print()
        print(self.turn + "'s Player Turn")
        pos = input('Choose a position from 1 to 9: ')

        try:
            pos = int(pos) - 1
        except:
            print('Please enter a valid position')

        if pos <= 9 and self.isValid(pos):
            self.board[pos] = self.turn
            self.turn = 'X' if self.turn == 'O' else 'O'
            self.displayBoard()

        else:
            print('=================================')
            print('| Please enter a valid position |')
            print('=================================')

    
    # return True if selected position is empty
    def isValid(self, position):
        return self.board[position] == ' '


    # Return True if any column, row or diagonal have same sign
    def isOver(self):
        if self.checkRow():
            return True
        if self.checkColumn():
            return True
        if self.checkDiagonal():
            return True
        return False


    # return True if any of the row have same sign
    def checkRow(self):
        for i in range(0, 9, 3):
            if (self.board[i] == self.board[i+1]) and (self.board[i+1] == self.board[i+2]) and (self.board[i] == 'X' or self.board[i] == 'O'):
                self.winner = self.board[i]
                self.isContinue = False
                return True


    # return True if any of the column have same sign
    def checkColumn(self):
        for i in range(3):
            if (self.board[i] == self.board[i+3]) and (self.board[i+3] == self.board[i+6]) and (self.board[i] == 'X' or self.board[i] == 'O'):
                self.winner = self.board[i]
                self.isContinue = False
                return True

    # return True if either of diagonal have same sign
    def checkDiagonal(self):
        if (self.board[0] == self.board[4]) and (self.board[4] == self.board[8]) and (self.board[4] == 'X' or self.board[4] == 'O'):
            self.winner = self.board[4]
            self.isContinue = False
            return True

        if (self.board[2] == self.board[4]) and (self.board[4] == self.board[6]) and (self.board[4] == 'X' or self.board[4] == 'O'):
            self.winner = self.board[4]
            self.isContinue = False
            return True


    # Return True is all places have filled
    def isTie(self):
        if not (' ' in self.board):
            self.isContinue = False


# Starting the main program
while True:

    print("=============================")
    print("Choose any of the following")
    print("1 for Single Player")
    print("2 for Multiplayer")
    print("Any other key to exit")
    playerMode = input("Choose: ")

    if not (playerMode == '1' or playerMode == '2'):
        print("================== Thankyou !! ==================")
        break

    game = Game()
    game.play(playerMode)
