package com.company;

public class Main {

    public static void main(String[] args) {


        //int highScore = calculateScore(true, 800, 5, 100);

        //calculateScore(true, 10000, 8, 200);
        int position = calculateHighScore(1500);
        displayHighScorePosition("Tim", position);

        position = calculateHighScore(900);
        displayHighScorePosition("Bob", position);

        position = calculateHighScore(200);
        displayHighScorePosition("Percy", position);

        position = calculateHighScore(50);
        displayHighScorePosition("Gilbert", position);

        position = calculateHighScore(1000);
        displayHighScorePosition("Louis", position);


    }

    public static int calculateScore(boolean gameOver, int score,
                                      int levelCompleted,
                                      int bonus){

        if (gameOver) {
            int finalScore = score + (levelCompleted * bonus);
            finalScore+=2000;
            System.out.println("Your final score was "+ finalScore);
            return finalScore;
        }
        return -1;

    }
    public static void displayHighScorePosition(String playerName,
                                                int position){
        System.out.println(playerName + " managed to get into position " +
                position + " on the high score table.");

    }
    public static int calculateHighScore (int score){

//        if (score>=1000){
//            return 1;
//        }else if (score >= 500){
//            return 2;
//        }else if (score >= 100){
//            return 3;
//        }
//
//        return 4;
        int position = 4;
        if (score >=1000) {
            position = 1;
        } else if (score >= 500){
            position = 2;
        } else if (score >= 100){
            position = 3;
        }
        return position;

    }
}
