'''
CMPT 120 Intro to Programming
Chapter 11 lab: Lists and Error Handling
Author: Erin Alvarico
Created: November 2nd, 2018
'''

firstRow = [0, 0, 0]
middleRow = [0, 0, 0]
lastRow = [0, 0, 0]

board = [firstRow, middleRow, lastRow]
# TODO replace this with a list containing 3 elements, each one being a list of 3 zeroes

symbol = [" ", "x", "o"]
# used to print out the board to the user

def printRow(row):

    print("|", end="")

    for i in range(3):
        print(" " + symbol[row[i]] + " " + "|", end="")

    print(end='\n')
    # this will start a new line on next print.


def printBoard(board):

    print("+-----------+")

    for i in range(3):
        printRow(board[i])
        print("+----------+")

def markBoard(board, row, col, player):

    if board[row][col] == 0:
        board[row][col] = player
    else:
        print("[ ERROR: Space is taken! ]")

def getPlayerMove():

    row = int(input("Pick a row: "))-1
    col = int(input("Pick a col: "))-1

    return (row, col)

def hasBlanks(board):

    isBlank = False

    for r in range(len(board[0])):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                isBlank = True

    return isBlank

def checkWinner(player):
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            print(symbol[player], " wins!")
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            print(symbol[player], " wins!")
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(symbol[player], " wins!")
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(symbol[player], " wins!")
        return True


def main():

    player = 1

    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        markBoard(board,row,col,player)

        if checkWinner(player):
            break

        player = player % 2 + 1


main()