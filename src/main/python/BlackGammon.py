from Player import Player
from ComputerPlayer import ComputerPlayer
import copy
import random

class Blackgammon():

    whitePlayer = Player()
    blackPlayer = Player()

    # Constants for self.white and self.black
    white = "white"
    black = "black"

    # Using the variable gives mean when you read the code and makes it easier to change.
    # so if your code read numberOfChips less than 15 what does this mean, numberOfChips less then totalChips
    totalChips = 15
    middleOfBoard = 13
    maxChipsOnPoint = 5

    # Define home, start and middle for self.white and self.black, this gives more meaning when you read the code
    # reading numbers is difficult to understand
    home = {white:25,black:0}
    start = {white:0,black:25}
    middle = {white:26,black:27} # We need to record self.white/self.black chips moved off the board
    dice = []

    # Create initial setup board
    # We have a fixed number of columns that can either be self.white or self.black
    # A data structure to store the board could be a list
    # For each element we need to store the colour and number of chips
    initialBoard = [[None,0],
                    [white,2],[None,0],[None,0],[None,0],[None,0],[black,5],
                    [None,0],[black,3],[None,0],[None,0],[None,0],[white,5],
                    [black,5],[None,0],[None,0],[None,0],[white,3],[None,0],
                    [white,5],[None,0],[None,0],[None,0],[None,0],[black,2],
                    [None,0],
                    [None,0],
                    [None,0]
                   ]

    def displayMiddleBoard(self,board,player):
        player.displayToPlayer()
        player.displayToPlayer()
        if board[self.middle[self.white]][1] > 0 or board[self.middle[self.black]][1] > 0:
            player.displayToPlayer("Middle has " + str(board[self.middle[self.white]][1]) + " self.white chips in the middle please type" + str(self.middle[self.white]))
            player.displayToPlayer("Middle has " + str(board[self.middle[self.black]][1]) + " self.black chips in the middle please type" + str(self.middle[self.black]))
            player.displayToPlayer()

    def displayCounterIndex(self,startPoint,endPoint,player):
        for counter in range(startPoint,endPoint):
            if counter == startPoint + ((endPoint - startPoint) // 2):
                player.displayToPlayer("  ",ending="")
            if counter >= 10:
                player.displayToPlayer("    " + str(counter) + "  ",ending="")
            else:
                player.displayToPlayer("   " + str(counter) + "    ",ending="")
        player.displayToPlayer()

    # We want to keep one thing together so we displayBoard
    # This method could do with refactoring and improving
    def displayBoard(self,board,player):
        for counter, point in enumerate(board):

            # Create a new line if on the second half
            # We also add any chips in the middle
            if counter == self.middleOfBoard:
                self.displayMiddleBoard(board,player)
                self.displayCounterIndex(self.middleOfBoard,self.home[self.white],player)

            # We create a divide for the mid part of the game
            # The equation is probably excessive and hardcoded values would be better,
            # but it means if the board changes it still works
            if (counter == ((self.middleOfBoard - self.home[self.black])//2)+1) or (counter == self.middleOfBoard + ((self.home[self.white]-self.middleOfBoard)//2)):
                player.displayToPlayer("||",ending =" ")

            if counter == 0:
                player.displayToPlayer("self.black Home has " + str(point[1]))
                self.displayCounterIndex(self.home[self.black]+1,self.middleOfBoard,player)
            elif counter == 25:
                player.displayToPlayer()
                player.displayToPlayer("self.white Home has " + str(point[1]))
                player.displayToPlayer()
            elif counter < 25:
                # To make the length of colour so the counter matches up we add a space to None
                if point[0] == None:
                    colour = "None "
                else:
                    colour = point[0]
                player.displayToPlayer(colour + " " + str(point[1]),ending=" ")



    def throwADie(self):
        return random.randint(1,6)

    def throwDice(self):
        self.dice.clear
        self.dice.append(self.throwADie())
        self.dice.append(self.throwADie())
        # If we roll the same dice the player gets four moves
        if self.dice[0] == self.dice[1]:
            self.dice.append(self.dice[0])
            self.dice.append(self.dice[0])

        return self.dice

    def displayDice(self,dice, colour):
        print(colour + " rolled:")
        for die in dice:
            print(die)

    def requestPlayerMove(self,colour, dice,player):
        numberOfMoves = 0
        pointToMoveFrom = player.getPlayerPosition(colour,player,self.middle[self.black])
        # A negative pointToMoveFrom indicates the players wants to stop
        if pointToMoveFrom >= 0:
            numberOfMoves = player.getPlayerDieToMove(colour,dice,player)
        return pointToMoveFrom, numberOfMoves

    # Determine the direction of the move
    # self.white moves forward
    # Balck moves back so we subtract
    def determineNewPosition(self,colour,pointToMoveFrom, numberOfMoves):
        # Determine the direction of the move
        # self.white moves forward
        # Balck moves back so we subtract

        #If we are in the middle we need to reset
        if pointToMoveFrom == self.middle[colour]:
            pointToMoveFrom = self.start[colour]

        # If the move is beyond, further, than home we make it home
        if colour == self.white:
            newPosition = pointToMoveFrom + numberOfMoves
            if newPosition > self.home[colour]:
                newPosition = self.home[colour]
        else:
            newPosition = pointToMoveFrom - numberOfMoves
            if newPosition < self.home[colour]:
                newPosition = self.home[colour]

        return newPosition

    def dieExists(self,dice,numberOfMoves):
        return numberOfMoves in dice

    def validatePointToMoveFrom(self,currentBoard,colour,point,silent ):
        valid = True
        if not point <= self.middle[colour]:
            if not silent:
                print("Point is too large")
            valid = False
        elif not currentBoard[point][0] == colour:
            if not silent:
                print("Position to move from not your colour")
            valid = False
        elif not currentBoard[point][1] > 0:
            if not silent:
                print("Position to mover from does not have sufficient chips")
            valid = False
        elif currentBoard[self.middle[colour]][1]> 0 and not point == self.middle[colour]:
            if not silent:
                print("You have chips in the middle, please play these first")
            valid = False

        return valid

    def allInHome(self,currentBoard,colour):
        total = 0
        # We need to create a direction for the range, since home is zero for self.black and 25 for self.white
        # So for self.white we go backwards
        direction = 1
        if colour == self.white:
            direction = -1

        for counter in range(self.home[colour],self.determineNewPosition(colour,self.home[colour],-7),direction):
            if currentBoard[counter][0] == colour:
                total += currentBoard[counter][1]
        return total == self.totalChips

    # We need to validate the point to move to
    def validatePointToMoveTo(self,currentBoard,colour,point,silent ):
        valid = True
        if currentBoard[point][0] != colour and currentBoard[point][0] != None and not currentBoard[point][1] == 1:
            if not silent:
                print("Position is not your colour and has more than one chip")
            valid = False
        elif not (currentBoard[point][0] == colour or currentBoard[point][0] == None or currentBoard[point][1] == 1):
            if not silent:
                print("Position to move to is not your colour or no colour")
            valid = False
        elif point != self.home[colour] and not (currentBoard[point][1] < self.maxChipsOnPoint):
            if not silent:
                print("You can only have a maximum of", self.maxChipsOnPoint, "chips on a point")
            valid = False
        elif point%25 == 0 and not self.allInHome(currentBoard,colour):
            if not silent:
                print("Not able to move off the board till all chips are home")
            valid = False
        return valid

    def validPlayerInstructions(self,currentBoard,colour,dice,pointToMoveFrom, numberOfMoves, silent=False):
        # Assume it is valid
        # We can then have a number of nots to check if valid and set not with feedback
        valid = True
        if not self.dieExists(dice,numberOfMoves):
            print("Die does not exist")
            valid = False

        if not self.validatePointToMoveTo(currentBoard,colour,self.determineNewPosition(colour,pointToMoveFrom, numberOfMoves),silent):
            valid = False

        if not self.validatePointToMoveFrom(currentBoard,colour,pointToMoveFrom,silent):
            valid = False

        return valid

    def playerCanMove(self,currentBoard,colour,dice):
        canMove = False
        counter = 0
        # We use a while so we can exit once the player can move, this is faster than doing a for every move
        while counter < len(currentBoard) and not canMove:
            if currentBoard[counter][0] == colour:
                for die in dice:
                    if self.validPlayerInstructions(currentBoard,colour,dice,counter,die,True):
                        canMove = True
            counter += 1
        return canMove

    def validPlayerRound(self,currentBoard,colour,dice,player):
        valid = False
        pointToMoveFrom, numberOfMoves = self.requestPlayerMove(colour,dice,player)
        while pointToMoveFrom >= 0 and self.playerCanMove(currentBoard,colour,dice) and not valid:
            if self.validPlayerInstructions(currentBoard,colour,dice,pointToMoveFrom, numberOfMoves):
                valid = True
            else:
                print("Please try again")
                pointToMoveFrom, numberOfMoves = self.requestPlayerMove(colour,dice,player)

        return pointToMoveFrom, numberOfMoves

    def makePlayerMove(self,currentBoard,colour,pointToMoveFrom, numberOfMoves):
        #Decrement chip from position to move from
        positionFromCount = currentBoard[pointToMoveFrom][1]-1
        positionFromColour = colour
        if positionFromCount == 0:
            positionFromColour = None
        currentBoard[pointToMoveFrom] = [positionFromColour,positionFromCount]
        # Determine the direction of the move
        # self.white moves forward
        # self.black moves back so we subtract
        newPosition = self.determineNewPosition(colour,pointToMoveFrom, numberOfMoves)
        originalColour = currentBoard[newPosition][0]
        if currentBoard[newPosition][0] != None and currentBoard[newPosition][0] != colour:
            currentBoard[self.middle[originalColour]] = [originalColour,currentBoard[self.middle[originalColour]][1] + 1]
            currentBoard[newPosition][1] = 0
        currentBoard[newPosition] = [colour,currentBoard[newPosition][1]+1]
        return currentBoard

    def playerRound(self,currentBoard,colour,dice,player):
        pointToMoveFrom = 0
        # We don't know how many dice they have or if the try to exit with a negative pointToMoveFrom
        # So we need a conditional while to loop
        while len(dice) > 0 and pointToMoveFrom >= 0:
            pointToMoveFrom, numberOfMoves = self.validPlayerRound(currentBoard,colour,dice,player)
            currentBoard = self.makePlayerMove(currentBoard,colour,pointToMoveFrom, numberOfMoves)
            self.displayBoard(currentBoard,player)
            if pointToMoveFrom >= 0:
                dice.remove(numberOfMoves)
        return currentBoard, pointToMoveFrom

    def playGameForColour(self,currentBoard,colour,player):
        dice = self.throwDice()
        print("New turn for",colour)
        self.displayBoard(currentBoard,player)
        self.displayDice(dice,colour)
        if self.playerCanMove(currentBoard,colour,dice):
            currentBoard, pointsToMoveFrom = self.playerRound(currentBoard,colour,dice,player)
        else:
            print(colour + " has no moves")
            pointsToMoveFrom = 0
        return currentBoard, pointsToMoveFrom

    def playGame(self,currentBoard):
        pointsToMoveFrom = 0
        print("To exit enter a negative position to move from")
        # We need to iterate to keep till one player has all chips home or someone tries to exit with a negative pointToMoveFrom
        # So we need to iterate with a while since it is conditional
        while (currentBoard[self.home[self.white]][1] != self.totalChips and currentBoard[self.home[self.black]][1] != self.totalChips) and pointsToMoveFrom >=0:
            currentBoard,pointsToMoveFrom = self.playGameForColour(currentBoard,self.white,self.whitePlayer)
            if pointsToMoveFrom >= 0:
                currentBoard,pointsToMoveFrom = self.playGameForColour(currentBoard,self.black,self.blackPlayer)

    def main(self):
        # We need to make a deep copy or whe we change the currentBoard we will also change the initialBoard
        # It is a memory address to the same list
        currentBoard = copy.deepcopy(self.initialBoard)
        playComputer = input("Do you want to play against the computer?")
        if playComputer[0].upper() == "Y":
            howGood = self.whitePlayer.requestIntegerFromPlayer("Please choose how good the computer is from 1 to 3")
            self.whitePlayer = ComputerPlayer(self,currentBoard,self.dice,self.white,howGood)
        self.playGame(currentBoard)

if __name__ == "__main__":
    blackgammon = Blackgammon()
    blackgammon.main()
