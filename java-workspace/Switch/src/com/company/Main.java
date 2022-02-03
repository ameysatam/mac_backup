package com.company;

import java.util.Locale;

public class Main {

    public static void main(String[] args) {
//	    int value = 3;
//        if(value ==1) {
//            System.out.println("Value was 1");
//        } else if (value == 2) {
//            System.out.println("Value was 2");
//        } else {
//            System.out.println("Was not 1 or 2");
//        }

//        int switchValue = 3;
//        switch(switchValue) {
//            case 1:
//                System.out.println("Value was 1");
//                break;
//
//            case 2:
//                System.out.println("Value was 2");
//                break;
//
//            case 3: case 4: case 5:
//                System.out.println("was a 3, or a 4 or a 5");
//                System.out.println("Actually it was "+switchValue);
//                break;
//
//            default:
//                System.out.println("Was not 1 or 2");
//                break;
            char charValue = 'V';
            switch(charValue){
                case 'A':
                    System.out.println("Value was A: "+charValue);
                    break;

                case 'B':
                    System.out.println("Value was B: "+charValue);
                    break;
                case 'C':
                    System.out.println("Value was C: "+charValue);
                    break;
                case 'D':
                    System.out.println("Value was D: "+charValue);
                    break;
                case 'E':
                    System.out.println("Value was E: "+charValue);
                    break;
                default:
                    System.out.println("Was neither A, B, C, D or E: "+charValue);
                    break;

            }
            String month = "JANUARY";
            switch(month.toLowerCase()){
                case "january":
                    System.out.println("Jan");
                    break;
                case "july":
                    System.out.println("July");
                    break;
                default:
                    System.out.println("Not sure!!");
                    break;
            }
        }

        //More code here
}
