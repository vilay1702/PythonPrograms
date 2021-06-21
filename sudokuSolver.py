def isValid(board, x, y, value):
    for i in range(len(board[0])):
        if board[x][i] == value:
            return False
    for i in range(len(board)):
        if board[i][y] == value:
            return False 

    smi = (x//3)*3
    smj = (y//3)*3

    for i in range(3):
        for j in range(3):
            if board[smi+i][smj+j] == value:
                return False 
    
    return True

def display(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end="  ")
            if j==2 or j==5:
                print("|", end="  ")
        print()
        if i==2 or i==5:
            print('-'*31)
    print()

def solveSudoku(board, i, j):
    # Base Condition
    if i == len(board[0]):
        display(board)
        return

    # Setting next position to be access
    ni = 0
    nj = 0
    if j == len(board[0])-1:
        ni = i+1
        nj = 0
    else:
        ni = i
        nj = j+1

    # print("i:{}, j:{}, ni:{}, nj:{}".format(i, j, ni, nj))
    # if position is already filled then move to next position 
    if board[i][j] != 0:
        solveSudoku(board, ni, nj)
    # else check for possible option 
    else:
        for pos in range(1,10):
            if isValid(board, i, j, pos):
                board[i][j] = pos 
                solveSudoku(board, ni, nj)
                board[i][j] = 0


if __name__ == "__main__":

    sudoku = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]

    # User input sudoku 
    # sudoku = []
    # for _ in range(9):
    #     userinput = list(map(int, input().strip().split()))
    #     sudoku.append(userinput)

    print(solveSudoku(sudoku, 0, 0))