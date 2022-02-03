package com.company;

public class Main {

    public static void main(String[] args) {
        byte ameyByte = 10;
        short ameyShort = 20;
        int ameyInt = 50;
        long ameyLong;
        ameyLong = 50000 + 10*(ameyByte + ameyShort+ameyInt);
        System.out.println("Amswer is :" + ameyLong);

        short shortTotal = (short)(50000L + 10L*(ameyByte + ameyShort+ameyInt));
        System.out.println(shortTotal);
    }
}
