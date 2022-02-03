package com.company;

public class Main {

    public static void main(String[] args) {
        System.out.println(sumFirstAndLastDigit(-5));
    }
    public static int sumFirstAndLastDigit(int number){
        boolean isNegative = false;
        if (number<0){
            isNegative = true;
            number = -1*number;
        }
        int reverse = 0;
        System.out.println("number = "+number);
        int temp = number;
        while (temp>0){
            int digit = temp%10;
            System.out.println("digit = "+digit);
            reverse = (reverse*10)+digit;
            System.out.println("Reverse = "+reverse);
            temp/=10;
        }
        if (isNegative){
            return -1*(number%10+reverse%10);
        } else{
            return number%10+reverse%10;
        }

    }
}
