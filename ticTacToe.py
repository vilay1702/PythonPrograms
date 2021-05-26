import random 
import math

class Game:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.winner = None 


    def __str__(self):
        return str(''.join(self.board))

        
    def displayBoard(self):
        print()
        print('\t' + self.board[0], '|', self.board[1], '|', self.board[2])
        print('\t' + '--+---+--')
        print('\t' + self.board[3], '|', self.board[4], '|', self.board[5])
        print('\t' + '--+---+--')
        print('\t' + self.board[6], '|', self.board[7], '|', self.board[8])
        print()


    def isValid(self, position):
        return self.board[position] == ' '


    def makeMove(self, letter, position):
        self.board[position] = letter


    def isFull(self):
        if (' ' in self.board):
            return False
        else:
            return True


    def convertPosition(self, position):
        return (position-1)
    

    # return True if any of the row have same sign
    def checkRow(self, board):
        for i in range(0, 9, 3):
            if (board[i] == board[i+1]) and (board[i+1] == board[i+2]) and (board[i] == 'X' or board[i] == 'O') and (self.winner != None):
                self.winner = board[i]
                return True
        return False


    # return True if any of the column have same sign
    def checkColumn(self, board):
        for i in range(3):
            if (board[i] == board[i+3]) and (board[i+3] == board[i+6]) and (board[i] == 'X' or board[i] == 'O') and (self.winner != None):
                self.winner = board[i]
                return True
        return False


    # return True if either of diagonal have same sign
    def checkDiagonal(self, board):
        if (board[0] == board[4]) and (board[4] == board[8]) and (board[4] == 'X' or board[4] == 'O') and (self.winner != None):
            self.winner = board[4]
            return True 

        if (board[2] == board[4]) and (board[4] == board[6]) and (board[4] == 'X' or board[4] == 'O') and (self.winner != None):
            self.winner = board[4]
            return True
        return False 


    def isWinner(self, board):
        if(self.checkRow(board) or self.checkColumn(board) or self.checkDiagonal(board)):
            return True
        else:
            return False 


    def playerMove(self):
        # print('____________________________')
        while True:
            print()
            print("X's Player Turn")
            pos = input('Choose a position from 1 to 9: ')

            try:
                pos = int(pos) 

                pos = self.convertPosition(pos)

                if ((pos>0) or (pos < 9)) and self.isValid(pos):
                    self.makeMove('X', pos)
                    # self.displayBoard()
                    return 

                else:
                    print('+-------------------------------+')
                    print('| Please enter a valid position |')
                    print('+-------------------------------+')
                    self.displayBoard()
                
            except:
                print('+-------------------------------+')
                print('| Please enter a valid position |')
                print('+-------------------------------+')
                self.displayBoard()

    def computerMove(self):
        move = -1
        possibleMoves = [x for x, letter in enumerate(self.board) if letter == ' ']

        for m in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = self.board[:]
                boardCopy[i] = m 
                if self.isWinner(boardCopy):
                    move = i 
                    # return move 
                    self.makeMove('O', move)
                    return
            corners = []    
            for i in possibleMoves:
                if i in [0, 2, 6, 8]:
                    corners.append(i)

            if len(corners) > 0:
                move = random.choice(corners)
                # return move 
                self.makeMove('O', move)
                return

            if 5 in possibleMoves:
                move = 5
                # return move
                self.makeMove('O', move)
                return

            edges = []
            for i in [1, 3, 5, 7]:
                edges.append(i)
            
            if len(edges) > 0:
                move = random.choice(edges)
                # return move
                self.makeMove('O', move)
                return


    def play(self):
        while True:
            self.displayBoard()
            self.playerMove()
            self.computerMove()
            print(self.board)

            print(self.isWinner(self.board))
            if self.isWinner(self.board):
                return
            if not(' ' in self.board):
                print('+---------------+')
                print('| GAME IS TIE!! |')
                print('+---------------+')
                return 
        
        


# =================== Main ===================

print('+-------------------------------+')
print('|            Welcome            |')
print('+-------------------------------+') 

isRematch = True
while isRematch:
    g = Game()
    g.play()

    userChoice = input("Enter 1 to rematch and any other key to exit: ")
    if userChoice != "1":
        isRematch = False
