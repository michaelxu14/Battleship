""" Complete your "Project Details".  If there is an arrow to the right of the line number then click the arrow
to expand the comment.
********************************************************
COMP 1005/1405 Section [Code] - Assignment 3

Project Details:
    Name: Michael Xu
    Student #: 101332292
    Date Created: Oct 26, 2024

External Libraries Used (if appliable)
random
********************************************************


"""
""" Pseudocode 
        Prompt user input for total rounds of the game
        Initialize the total game score
        for each round:
            Validate the user input for board size and number of ships
            Handle invalid entries 
            Set the board and ships.
            for each shot in the round:
                Request the user to input the assumed ship coordinates
                Display the Hit message (Hit or Miss)
                Display the full board with updated attempts results 
            Show the final state of the board
            Display the user final score of this round
        Display the user final score of the game
"""

""" Import the libraries if appliable
"""
import random

""" Define global variables if appliable
"""

totalScore = 0
round = 0

# Suggest to start by understanding the code in the main function.
# Then proceed with the coding.


def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
            Randomly places the user-specified number of ships (“S”) on the board.
        Parameter(s): 
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None   
    """

    size = len(board)  
    placed_ships = 0   
 
    while placed_ships < numShips:
        randX = random.randint(0, size-1) #as the coordinates begin at 0 on the board
        randY = random.randint(0, size-1)
        # to make sure that there is no overlapping, only squares with '~' are made ships
        if board[randX][randY] == '~':
            board[randX][randY] = 'S'
            placed_ships += 1
        
    return board

#TESTED
def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s): 
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """

    
    sizeVal = False
    shipVal = False

    # minimum board size should be 2x2, maximum should be 5x5
    if size < 2 or size > 5:
        sizeVal = True
    # maximum ship number should be size^2 - 2, min should be 1
    if numShips <= 0 or numShips >= size**2 - 2:
        shipVal = True

    if sizeVal == True or shipVal == True:
        print("Invalid input")
        return True
    else:
        return False


# TESTED
def checkFireError(board, row, col):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return [Boolean]: Return True if an error is found or False if there is no error.   
    """

    size = len(board)
    # check if the row and column are within the bounds of the board
    
    if row < 0 or row >= size or col < 0 or col >= size:
        print("Error, out of bounds")
        return True
    # check if the selected spot has already been shot at
    if (board[row][col] == 'X') == True or (board[row][col] == 'O') == True:
        print("Error, this spot has already been inputted")
        return True
    
    return False

#TESTED
def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists  
    """
    board = []
    for i in range(size):
        row = []  
        # inner loop to fill each cell in the row with '~'
        for j in range(size):
            row.append('~')
        # append the completed row to the board
        board.append(row)
    
    return board
   

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.
        
        Return: None  
    """

     #iterate through 2 dimensional list board
    for row in board:
        for cell in row:
            if round and cell == 'S':
            # hide ships during the round
                print('~', end=' ')  
            else:
            # show everything else
                print(cell, end=' ')  
        print()  


def fireShot(board, row, col):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.     
    """  
    hit = board[row][col]
    #check if board[row][col] is indeed a S
    if hit == 'S':
        return True
    else:
        return False

def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round 
            
            Pseudocode:
            Keep track of number of shots for the round
            Keep track of the score (number of hits) for the round
            Loop until user fires all their shots
                Ask user to enter coordinates for their shot.  Input two numbers separated by a space.
                Validate the shot coordinates using checkFireError function
                Fire a shot using the fireShot function
                Output if the shot is a hit or a miss
                display the board after the shot has been taken displayBoard(board)
            Output "End of round X"
            display the board at the end of the round displayBoard(board, False)
    
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.   
    """

    # Keep track of number of shots for the round
    shotsTaken = 0
    # Keep track of the score (number of hits) for the round
    hits = 0
    # maximum shots allowed, based on board size (TEST PURPOSES)
    #maxShots = len(board) * len(board)  
    # maximum shots (real)
    maxShots = int(len(board) * len(board) * 0.25 + 2)
    #print(maxShots)
    global round
    round += 1

    # loop until user fires all their shots or all ships are hit
    while shotsTaken < maxShots and hits < numShips:

        #print(board)
        
        # ask the user to enter coordinates for their shot
        coords = input("Enter the coordinates for your shot (row col) \n")
        row, col = coords.split(" ") #easy short way to assign both
        row = int(row)
        col = int(col)

        # validate the shot coordinates using checkFireError 
        if checkFireError(board, row, col):
            continue  

        # fire a shot using the fireShot function
        if fireShot(board, row, col):
            print("Hit!")
            board[row][col] = 'X'  
            hits += 1
        else:
            print("Miss!")
            board[row][col] = 'O'  

        shotsTaken += 1
        # display the board after the shot has been taken
        displayBoard(board)


    # output "End of round X"
    print(f"End of round {round}")

    # display the final board at the end of the round
    displayBoard(board, round=False)

    # Return the number of hits for the round
    return hits




def main():    
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None  
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return



if __name__ == '__main__':
    main()
