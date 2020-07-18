import random

class ComputerPlayer():

    backgammon = None
    currentBoard = None
    dice = None
    colour = None
    howGood = 0
    playerMove = 0
    playerPosition = 0

    def __init__(self,backgammon,currentBoard,dice,colour,howGood):
        self.backgammon = backgammon
        self.currentBoard = currentBoard
        self.dice = dice
        self.colour = colour
        self.howGood = howGood

    def determinePositionAndMove(self,forward):
        if forward:
            counter = 0
            direction = 1
        else:
            counter = len(self.currentBoard) -1

        foundAGoodMove = False
        while 0 <= counter < len(self.currentBoard) and not foundAGoodMove:
            if self.currentBoard[counter][0] == self.colour:
                diceCounter = 0
                while diceCounter < len(self.dice) and not foundAGoodMove:
                    die = self.dice[diceCounter]
                    if self.backgammon.validPlayerInstructions(self.currentBoard,self.colour,self.dice,counter,die,True):
                        self.playerPosition = counter
                        self.playerMove = die
                        if self.currentBoard[self.backgammon.determineNewPosition(self.colour,counter,die)] == 1:
                            foundAGoodMove = True
                    diceCounter += 1
            if forward:
                counter += 1
            else:
                counter -= 1

    def rankingMove(self):
        if self.howGood == 1:
            self.determinePositionAndMove(True)
        elif self.howGood == 2:
            self.determinePositionAndMove(False)
        elif self.howGood == 3:
            if random.randint(0,2) == 1:
                self.determinePositionAndMove(True)
            else:
                self.determinePositionAndMove(False)

    def getPlayerPosition(self,colour,player,maxPosition):
        self.rankingMove()
        return self.playerPosition

    def getPlayerDieToMove(self,colour,dice,player):
        return self.playerMove

    def displayToPlayer(self,message="",ending=""):
        pass
