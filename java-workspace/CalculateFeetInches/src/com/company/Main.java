package com.company;

public class Main {

    public static void main(String[] args) {
        calcFeetAndInchesToCentimeters(157);
    }

    public static double calcFeetAndInchesToCentimeters(double feet, double inches){
        if (feet>=0 && inches>=0 && inches<=12){

            double centimeters =  (feet*12*2.54 + inches*2.54);
            System.out.println(feet + " ft "+ inches+" inches = "+ centimeters+ " cm.");
            return centimeters;
        }
        else {
            System.out.println("Invalid feet or inches parameters");
            return -1;
        }
    }
    public static double calcFeetAndInchesToCentimeters(double inches){
        if (inches>=0){
            double feet = (int) inches/12;
            double inches2 = (int)inches%12;
            System.out.println(inches + " inches has " + feet + " feet and " +inches2 +" inches.");
            return calcFeetAndInchesToCentimeters(feet, inches2);

        }
        else {
            System.out.println("Invalid feet or inches parameters");
            return -1;
        }
    }
}
