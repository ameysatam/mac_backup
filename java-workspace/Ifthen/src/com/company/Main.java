package com.company;

public class Main {

    public static void main(String[] args) {
        boolean isAlien = false;
        if (isAlien == false)
            System.out.println("It is not an alien!");

        if (2<3)
            System.out.println("2 is less than 3");

        if (9<10) {
            System.out.println("Why this kolavari");
            System.out.println("Kolavari kolavari di");
        }

        int topScore =80;
        if (topScore != 100){
            System.out.println("You got the high score!");
        }

        int secondTopScore = 60;
        if (topScore > secondTopScore && topScore <100){
            System.out.println("Greater than second top score and less than 100");
        }

        boolean isCar = false;
        if (isCar) {
            System.out.println("This is not supposed to happen");
        }
        isCar =true;
        boolean wasCar = isCar ? true : false;
        if (wasCar) {
            System.out.println("WasCar is true now");
        }
    }
}
