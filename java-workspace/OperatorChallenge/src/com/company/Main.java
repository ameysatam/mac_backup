package com.company;

public class Main {

    public static void main(String[] args) {
	    double doubleVariable =20.00d;
        double doubleVariable2 =80.00d;
        double doubleVariable3 = (doubleVariable + doubleVariable2)*100.00d;
        System.out.println("MyValuesTotal = " + doubleVariable3);
        double doubleVariable4 = doubleVariable3 % 40.00d;
        System.out.println("thRemainder = " + doubleVariable4);
        boolean isTrue;
        isTrue = doubleVariable4==0.00 ? true:false;
        System.out.println(isTrue);
        if (!isTrue){
            System.out.println("Got some remainder");
        }

    }
}
