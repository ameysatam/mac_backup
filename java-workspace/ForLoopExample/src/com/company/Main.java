package com.company;

public class Main {

    public static void main(String[] args) {
//        System.out.println("10,000 at 2% interest ="+calculateInterest(10000,2));

//        for (int i = 2; i<=8; i++){
////            System.out.println("Loop "+i + " hello!");
//            System.out.println("10,000 at "+i+"% interest ="+String.format("%.2f",calculateInterest(10000,(double)i)));
//        }
//        System.out.println("**************************");
//        for (int j = 8; j>=2; j--){
////            System.out.println("Loop "+i + " hello!");
//            System.out.println("10,000 at "+j+"% interest ="+String.format("%.2f",calculateInterest(10000,(double)j)));
//        }
        isPrime_numberOfPrime(1000);
    }

    public static double calculateInterest(double amount, double interestRate){
        return (amount*(interestRate/100));
    }

    public static boolean isPrime(int n){

        if (n==1) {
            return false;
        }
        for (int i=2; i<=(double)Math.sqrt(n);i++){
            if (n%i ==0){
                return false;
            }
        }
        return true;
    }
    public static void isPrime_numberOfPrime(int n){
        int count =0;
        for (int j=n; j>1; j--){
            if (isPrime(j)) {
                count++;

            }

    }
        System.out.println("Is "+n+" a prime number?: "+isPrime(n)+". There are "+count+" prime numbers below "+n+".");
}
}
