package com.company;

public class Main {

    public static void main(String[] args) {
//        int count = 1;
//        while(count != 6) {
//            System.out.println("Count value is " + count);
//            count ++;
//        }
//
//        count =1;
//        while(true){
//            if (count == 6){
//                break;
//            }
//            System.out.println("Count value is " + count);
//            count++;
//        }
//        count =1;
//        do {
//            System.out.println("Count value is " + count);
//            count++;
//        }while (count <=6);
        int numberEven = 0;
        int number = 4;
        int finishNumber = 20;
        while (number<= finishNumber) {
            number++;
            if (!isEvenNumber(number)) {
                continue;
            }
            numberEven++;
            System.out.println("Even number = " + number);
            if (numberEven>=5) {
                break;
            }


        }
        int number1 = 0;
        while (number1<15){

            number1++;

            if (number1>=4 && number1<=7){
                System.out.println("Continue at "+number1);
                continue;
            }
            System.out.println("Number is "+number1);

            if (number1>=10&&number1<=13){
                System.out.println("COntinue at "+number1);
                continue;
            }
        }



    }
    public static boolean isEvenNumber(int number){
        if (number%2==0){
            return true;
        } else {
            return false;
        }
    }
}
