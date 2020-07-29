package java.src;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.src.PlayerInterface;

public class Player implements PlayerInterface{
    private String requestStringFromPlayer(String request) {

        Scanner userInput = new Scanner(System.in);
        String answer = userInput.nextLine();
        return answer;
    }

    private Integer requestIntegerFromPlayer(String request) {
        int result = 0;
        Boolean valid = false;

        do {
            try {
                result = Integer.parseInt(requestStringFromPlayer(request));
                valid = true;
            } catch (NumberFormatException exception) {
                // Output expected NumberFormatException.
                System.out.println("Please enter a integer");
            }
        } while (!valid);

        return result;
    }

    private String formatList(ArrayList<Integer> aList){
        String newString = "";
        String preFix = "";
        for (int item: aList){
            if (newString != "") {
                preFix = ",";
            }
            newString += preFix + Integer.toString(item);
        }
        return newString;
    }

    public Integer getPlayerPosition(String colour,Integer maxPosition) {
        Integer pointToMoveFrom = requestIntegerFromPlayer("Please enter position to move for " + colour);
        while (pointToMoveFrom <= maxPosition) {
            System.out.println("Postion does not exist, please try again");
            pointToMoveFrom = requestIntegerFromPlayer("Please enter position to move for " + colour);
        }
        return pointToMoveFrom;
    }

    public Integer getPlayerDieToMove(String colour, ArrayList<Integer> dice) {
        int numberOfMoves = requestIntegerFromPlayer("Please enter number of spaces to move for " + colour);
        String diceLeft = formatList(dice);
        while ( !dice.contains(numberOfMoves)) {
            System.out.println("Please select from " + diceLeft);
            numberOfMoves = requestIntegerFromPlayer("Please enter number of spaces to move for " + colour);
        }
        return numberOfMoves;
    }

    public void displayToPlayer(String message, String ending) {
        if (message == null){
            message = " ";
        }
        if (ending == null) {
            System.out.println(message);
        }
        else{
            System.out.print(message + ending);
        }
    }

}

