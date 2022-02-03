package com.company;

public class Main {

    public static void main(String[] args) {
        NumberInWord(0);
        NumberInWord(1);
        NumberInWord(2);
        NumberInWord(3);
        NumberInWord(4);
        NumberInWord(5);
        NumberInWord(6);
        NumberInWord(7);
        NumberInWord(8);
        NumberInWord(9);
        NumberInWord(10);
        NumberInWord(-1);
    }

    public static void NumberInWord (int number){
        switch(number){
            case 0:
                System.out.println("ZERO");
                break;
            case 1:
                System.out.println("ONE");
                break;
            case 2:
                System.out.println("TWO");
                break;
            case 3:
                System.out.println("THREE");
                break;
            case 4:
                System.out.println("FOUR");
                break;
            case 5:
                System.out.println("FIVE");
                break;
            case 6:
                System.out.println("SIX");
                break;
            case 7:
                System.out.println("SEVEN");
                break;
            case 8:
                System.out.println("EIGHT");
                break;
            case 9:
                System.out.println("NINE");
                break;
            default:
                System.out.println("other");


        }
    }
}
