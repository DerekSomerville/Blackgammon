package java.src;

import java.util.ArrayList;

public interface PlayerInterface {

    public Integer getPlayerPosition(String colour,Integer maxPosition);

    public Integer getPlayerDieToMove(String colour, ArrayList<Integer> dice);

    public void displayToPlayer(String message , String ending);
}
