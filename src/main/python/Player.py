class Player():

    def requestStringFromPlayer(self,request):
        return input(request)

    def requestIntegerFromPlayer(self,request):
        valid = False
        while not valid:
            try:
                answerAsString = self.requestStringFromPlayer(request)
                answerAsInteger = int(answerAsString)
                valid = True
            except ValueError:
                print("Please enter an integer")
        return answerAsInteger

    def getPlayerPosition(self,colour,maxPosition):
        pointToMoveFrom = self.requestIntegerFromPlayer("Please enter position to move for " + colour)
        while not pointToMoveFrom <= maxPosition:
            print("Postion does not exist, please try again")
            pointToMoveFrom = self.requestIntegerFromPlayer("Please enter position to move for " + colour)
        return pointToMoveFrom

    def getPlayerDieToMove(self,colour,dice):
        numberOfMoves = self.requestIntegerFromPlayer("Please enter number of spaces to move for " + colour)
        # We want to check the player enters one of the die
        while numberOfMoves not in dice:
            print("Please select from",dice)
            numberOfMoves = self.requestIntegerFromPlayer("Please enter number of spaces to move for " + colour)
        return numberOfMoves

    def displayToPlayer(self,message="",ending=None):
        if ending == None:
            print(message)
        else:
            print(message,end=ending)

