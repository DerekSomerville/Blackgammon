package java.src;

import java.src.PlayerInterface;
import java.src.Player;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class BlackGammon {
    PlayerInterface whitePlayer = new Player();
    PlayerInterface blackPlayer = new Player();
        
    int white = 0;
    int black = 1;
    int blank = 2;
    String[] colourName = {"white","black","none "};
    List<Integer> home = {25,0};
    List<Integer> start = {0,25};
    List<Integer> middle = {26,27};

    int totalChips = 15;
    int middleOfBoard = 13;
    int maxChipsOnPoint = 5;

    ArrayList<Integer> dice = new ArrayList<Integer>();
    
    ArrayList<List<Integer>> initialBoard = {{null,0}
            ,{white,2},{null,0},{null,0},{null,0},{null,0},{black,5}
            ,{null,0},{black,3},{null,0},{null,0},{null,0},{white,5}
            ,{black,5},{null,0},{null,0},{null,0},{white,3},{null,0}
            ,{white,5},{null,0},{null,0},{null,0},{null,0},{black,2}
            ,{null,0}
            ,{null,0}
            ,{null,0}};

    private void displayMiddleBoard(ArrayList<List<Integer>> board,Player player) {
        player.displayToPlayer();
        player.displayToPlayer();
        if ((board[this.middle[this.white]][1] > 0) or (board[ this.middle[this.black]][1] >0)) {
            player.displayToPlayer("Middle has " + Integer(board[this.middle[this.white]][1]).toString() + " white chips in the middle please type" + str(this.middle[this.white]));
            player.displayToPlayer("Middle has " + Integer(board[this.middle[this.black]][1]).toString + " black chips in the middle please type" + str(this.middle[this.black]));
            player.displayToPlayer();
        }
    }

    private void displayCounterIndex(int startPoint,int endPoint,Player player){
        for (int counter = startPoint; counter <= endPoint; counter++){
            if (counter == startPoint + ((endPoint - startPoint){
                player.displayToPlayer("  ","")
            }
            if (counter >= 10) {
                player.displayToPlayer("    " + Integer(counter).toString() + "  ", "")
            }
            else {
                player.displayToPlayer("   " + Integer(counter).toString() + "    ", "")
            }
            player.displayToPlayer()
        }
    }

    private void displayBoard(ArrayList<List<Integer>> board,Player player){
        for (int counter = 0; counter < board.size(); counter++) {
            List<Integer> point = board[counter];
            if (counter == this.middleOfBoard) {
                this.displayMiddleBoard(board, player);
                this.displayCounterIndex(this.middleOfBoard, this.home[this.white], player);
            }

            if (counter == ((this.middleOfBoard - this.home[this.black])/2)+1) Or (counter == this.middleOfBoard + ((this.home[this.white]-this.middleOfBoard)//2)):
                player.displayToPlayer("||"," ");

            if (counter == 0){
                player.displayToPlayer("this.black Home has " + Integer(point[1])).toString();
                this.displayCounterIndex(this.home[this.black]+1,this.middleOfBoard,player);
            }
            else if (counter == 25) {
                player.displayToPlayer();
                player.displayToPlayer("this.white Home has " + Integer(point[1]).toString()));
                player.displayToPlayer();
            }
            else if (counter < 25) {
                player.displayToPlayer(this.colourName[point[0]] + " " + Integer(point[1]).toString(), " ");
            }
        }
    }



    private int throwADie() {
        return random.randint(1, 6)
    }
    private throwDice(self):
    this.dice.clear
        this.dice.append(this.throwADie())
                this.dice.append(this.throwADie())
                # If we roll the same dice the player gets four moves
        if this.dice[0] == this.dice[1]:
            this.dice.append(this.dice[0])
            this.dice.append(this.dice[0])

            return this.dice

    private displayDice(dice, colour):
    print(colour + " rolled:")
        for die in dice:
    print(die)

    private requestPlayerMove(colour, dice,player):
    numberOfMoves = 0
    pointToMoveFrom = player.getPlayerPosition(colour,this.middle[this.black])
            # A negative pointToMoveFrom indicates the players wants to stop
        if pointToMoveFrom >= 0:
    numberOfMoves = player.getPlayerDieToMove(colour,dice)
            return pointToMoveFrom, numberOfMoves

    # Determine the direction of the move
    # this.white moves forward
    # Balck moves back so we subtract
    private determineNewPosition(colour,pointToMoveFrom, numberOfMoves):
            # Determine the direction of the move
        # this.white moves forward
        # Balck moves back so we subtract

        #If we are in the middle we need to reset
        if pointToMoveFrom == this.middle[colour]:
    pointToMoveFrom = this.start[colour]

            # If the move is beyond, further, than home we make it home
        if colour == this.white:
    newPosition = pointToMoveFrom + numberOfMoves
            if newPosition > this.home[colour]:
    newPosition = this.home[colour]
            else:
    newPosition = pointToMoveFrom - numberOfMoves
            if newPosition < this.home[colour]:
    newPosition = this.home[colour]

            return newPosition

    private dieExists(dice,numberOfMoves):
            return numberOfMoves in dice

    private validatePointToMoveFrom(currentBoard,colour,point,silent ):
    valid = True
        if not point <= this.middle[colour]:
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
    elif currentBoard[this.middle[colour]][1]> 0 and not point == this.middle[colour]:
            if not silent:
    print("You have chips in the middle, please play these first")
    valid = False

        return valid

    private allInHome(currentBoard,colour):
    total = 0
            # We need to create a direction for the range, since home is zero for this.black and 25 for this.white
        # So for this.white we go backwards
    direction = 1
            if colour == this.white:
    direction = -1

            for counter in range(this.home[colour],this.determineNewPosition(colour,this.home[colour],-7),direction):
            if currentBoard[counter][0] == colour:
    total += currentBoard[counter][1]
            return total == this.totalChips

    # We need to validate the point to move to
    private validatePointToMoveTo(currentBoard,colour,point,silent ):
    valid = True
        if currentBoard[point][0] != colour and currentBoard[point][0] != None and not currentBoard[point][1] == 1:
            if not silent:
    print("Position is not your colour and has more than one chip")
    valid = False
    elif not (currentBoard[point][0] == colour or currentBoard[point][0] == None or currentBoard[point][1] == 1):
            if not silent:
    print("Position to move to is not your colour or no colour")
    valid = False
    elif point != this.home[colour] and not (currentBoard[point][1] < this.maxChipsOnPoint):
            if not silent:
    print("You can only have a maximum of", this.maxChipsOnPoint, "chips on a point")
    valid = False
    elif point%25 == 0 and not this.allInHome(currentBoard,colour):
            if not silent:
    print("Not able to move off the board till all chips are home")
    valid = False
        return valid

    private validPlayerInstructions(currentBoard,colour,dice,pointToMoveFrom, numberOfMoves, silent=False):
            # Assume it is valid
        # We can then have a number of nots to check if valid and set not with feedback
    valid = True
        if not this.dieExists(dice,numberOfMoves):
    print("Die does not exist")
    valid = False

        if not this.validatePointToMoveTo(currentBoard,colour,this.determineNewPosition(colour,pointToMoveFrom, numberOfMoves),silent):
    valid = False

        if not this.validatePointToMoveFrom(currentBoard,colour,pointToMoveFrom,silent):
    valid = False

        return valid

    private playerCanMove(currentBoard,colour,dice):
    canMove = False
            counter = 0
        # We use a while so we can exit once the player can move, this is faster than doing a for every move
        while counter < len(currentBoard) and not canMove:
            if currentBoard[counter][0] == colour:
            for die in dice:
            if this.validPlayerInstructions(currentBoard,colour,dice,counter,die,True):
    canMove = True
    counter += 1
            return canMove

    private validPlayerRound(currentBoard,colour,dice,player):
    valid = False
            pointToMoveFrom, numberOfMoves = this.requestPlayerMove(colour,dice,player)
        while pointToMoveFrom >= 0 and this.playerCanMove(currentBoard,colour,dice) and not valid:
            if this.validPlayerInstructions(currentBoard,colour,dice,pointToMoveFrom, numberOfMoves):
    valid = True
            else:
    print("Please try again")
    pointToMoveFrom, numberOfMoves = this.requestPlayerMove(colour,dice,player)

            return pointToMoveFrom, numberOfMoves

    private makePlayerMoves(currentBoard,colour,moves):
            for move in moves:
            this.makePlayerMove(currentBoard,colour,move[0],move[1])
            return currentBoard

    private makePlayerMove(currentBoard,colour,pointToMoveFrom, numberOfMoves):
            #Decrement chip from position to move from
            positionFromCount = currentBoard[pointToMoveFrom][1]-1
    positionFromColour = colour
        if positionFromCount == 0:
    positionFromColour = None
    currentBoard[pointToMoveFrom] = [positionFromColour,positionFromCount]
            # Determine the direction of the move
        # this.white moves forward
        # this.black moves back so we subtract
    newPosition = this.determineNewPosition(colour,pointToMoveFrom, numberOfMoves)
    originalColour = currentBoard[newPosition][0]
            if currentBoard[newPosition][0] != None and currentBoard[newPosition][0] != colour:
    currentBoard[this.middle[originalColour]] = [originalColour,currentBoard[this.middle[originalColour]][1] + 1]
    currentBoard[newPosition][1] = 0
    currentBoard[newPosition] = [colour,currentBoard[newPosition][1]+1]
            return currentBoard

    private playerRound(currentBoard,colour,dice,player):
    pointToMoveFrom = 0
            # We don't know how many dice they have or if the try to exit with a negative pointToMoveFrom
            # So we need a conditional while to loop
        while len(dice) > 0 and pointToMoveFrom >= 0:
    pointToMoveFrom, numberOfMoves = this.validPlayerRound(currentBoard,colour,dice,player)
    currentBoard = this.makePlayerMove(currentBoard,colour,pointToMoveFrom, numberOfMoves)
            this.displayBoard(currentBoard,player)
            if pointToMoveFrom >= 0 and this.dieExists(dice,numberOfMoves):
            dice.remove(numberOfMoves)
            return currentBoard, pointToMoveFrom

    private playGameForColour(currentBoard,colour,player):
    dice = this.throwDice()
    print("New turn for",colour)
        this.displayBoard(currentBoard,player)
            this.displayDice(dice,colour)
            if this.playerCanMove(currentBoard,colour,dice):
    currentBoard, pointsToMoveFrom = this.playerRound(currentBoard,colour,dice,player)
            else:
    print(colour + " has no moves")
    pointsToMoveFrom = 0
            return currentBoard, pointsToMoveFrom

    private playGame(currentBoard):
    pointsToMoveFrom = 0
    print("To exit enter a negative position to move from")
        # We need to iterate to keep till one player has all chips home or someone tries to exit with a negative pointToMoveFrom
        # So we need to iterate with a while since it is conditional
        while (currentBoard[this.home[this.white]][1] != this.totalChips and currentBoard[this.home[this.black]][1] != this.totalChips) and pointsToMoveFrom >=0:
    currentBoard,pointsToMoveFrom = this.playGameForColour(currentBoard,this.white,this.whitePlayer)
            if pointsToMoveFrom >= 0:
    currentBoard,pointsToMoveFrom = this.playGameForColour(currentBoard,this.black,this.blackPlayer)

    private main(self):
            # We need to make a deep copy or whe we change the currentBoard we will also change the initialBoard
        # It is a memory address to the same list
            currentBoard = copy.deepcopy(this.initialBoard)
    playComputer = input("Do you want to play against the computer?")
        if playComputer[0].upper() == "Y":
    howGood = this.whitePlayer.requestIntegerFromPlayer("Please choose how good the computer is from 1 to 3")
    this.whitePlayer = ComputerPlayer(currentBoard,this.dice,this.white,howGood)
        this.playGame(currentBoard)
}
