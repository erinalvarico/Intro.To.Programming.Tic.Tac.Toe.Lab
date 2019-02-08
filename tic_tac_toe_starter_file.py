# CMPT 120 Intro to Programming
# Chapter 11 lab: Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD
board = [] # TODO replace this with a list containing 3 elements, each one being a list of 3 zeroes     
symbol = [ " ", "x", "o" ]  # used to print out the board to the user

#This function prints out one row of the tic tac toe board
def printRow(row):
# initialize output to the left border - a vertical dash
 print("|", end="")    # end="" keeps the output for the next print on the same line
# for each element in the "row" list passed as a parameter to this function:
    # Replace the question mark in the print statement below with correct symbol for this square(Hint: use the "symbol" list variable and row value--
    # Example: symbol[0] will print a blank, symbol[1] prints "x", and symbol[2] prints "o"
 print(" " + "?" + " " + "|", end="")  # this will keep everything on the same line (no line return after printing)
 print(end='\n') # this will start a new line on next print.

#This function prints out the current state of the tic tac toe board to the user
def printBoard(board):
# print the top border
 print("+-----------+")
# for each row in the board...
 
 printRow([0,0,0])  # Call "printRow()" but pass the list element for the current row as a parameter instead of "(0,0,0"
 print("+----------+")# print the next border

#This function "marks" the board with the player's move by storing a "1" for an "x" or a "2" for an "o" in the correct row and col.
def markBoard(board, row, col, player):
# check to see whether the desired square is blank (Hint: index the proper row and col of "board" and see if the value is equal to "0")
        # if True, store the "player" value in the list
        # if False, then print out a message stating the space has already been taken                  

#This function prompts the user for a row and col. Explain that valid values are 0, 1, and 2 for rows/columns 1, 2, and 3
def getPlayerMove():
 # prompt the user separately for the row and column numbers - remember to make the values integers!
 row = int(input(("pick a row"))
 col = int(input("pick a col"))
 return (row,col) # return the selected row and col values to "main()"

#This function checks to see if there are any remaining spaces left on the board.
def hasBlanks(board):
                # for each row in the board...
                   # for each col in the row...
                  
                     #If a space is available (represented by a "0" in the list element):
                        # return True
#If no square is blank, return False

# main function

def main():
 player = 1 # Start player out as "x" (indicated by a value of 1)
 while hasBlanks(board):
   printBoard(board)   # Print the current tic tac toe board out for the user to view
   #Call getPlayerMove which prompts the user for a row a column
   row,col = getPlayerMove()
   #Call markBoard which will set the appropriate spot to an "x" or "o", depending on the value of "player" (1 for x, 2 for o)
   markBoard(board,row,col,player)
   player = player % 2 + 1 # switch player for next turn  (1 becomes a 2 and a 2 becomes a 1)
main()
