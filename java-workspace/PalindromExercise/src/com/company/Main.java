package com.company;

public class Main {

    public static void main(String[] args) {
        System.out.println(isPalindrome(10));
    }

    public static boolean isPalindrome(int number)
    {
        if (number < 0)
        {
            number *= -1;
        }

        int reverse = 0;
        int stored = number; //121
        while (stored > 0)
        {
            // extract the lest-significant digit
            int digit = stored % 10; //digit = 1,2
            System.out.println("Digit = "+digit);
            reverse = (reverse * 10) + digit; //reverse = 1,12
            System.out.println("reverse = "+reverse);
            // drop the least-significant digit
            stored /= 10; //stored=12.1  // same as number = number / 10;
        }

        if (number == reverse)
        {
            return true;
        } else
        {
            return false;
        }

    }

    }

