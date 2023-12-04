package de.halberfan.adventofcode.y2023.day04;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Day04 {

    // Input: 10 - 26
    // Demo:   5 -  8

    static final int SIZE = 203;
    static String[] lines = new String[SIZE];
    static Card[] cards = new Card[SIZE];

    public static void main(String[] args) throws IOException {

        File file = new File("src/main/java/de/halberfan/adventofcode/y2023/day04/input.txt");
        FileReader fileReader = new FileReader(file);
        BufferedReader reader = new BufferedReader(fileReader);

        int c = 0;
        while (c < SIZE) {
            lines[c++] = reader.readLine();
        }

        partOne();
        partTwo();

    }

    private static void partOne() {

        int sum = 0;

        for (String line : lines) {
            line = line.substring(line.indexOf(':') + 2);
            Card card = new Card();

            boolean stillWinning = true;
            for (String s : line.split(" ")) {
                if (stillWinning) {
                    if (s.equals("|")) {
                        stillWinning = false;
                    } else {
                        if (!s.isEmpty()) card.winning.add(Integer.parseInt(s));
                    }
                } else {
                    if (!s.isEmpty()) card.have.add(Integer.parseInt(s));
                }
            }

            sum += card.getPoints();

        }

        System.out.println("Part 1: " + sum);

    }

    private static void partTwo() {
        int c = 0;
        for (String line : lines) {
            line = line.substring(line.indexOf(':') + 2);
            Card card = new Card();
            card.id = c;
            boolean stillWinning = true;
            for (String s : line.split(" ")) {
                if (stillWinning) {
                    if (s.equals("|")) {
                        stillWinning = false;
                    } else {
                        if (!s.isEmpty()) card.winning.add(Integer.parseInt(s));
                    }
                } else {
                    if (!s.isEmpty()) card.have.add(Integer.parseInt(s));
                }
            }

            cards[c++] = card;

        }

        int s = 0;
        for (Card card : cards) {
            s += card.getPointsForPartTwo();
        }

        System.out.println("Part 2: " + s);

    }

}

class Card {
    ArrayList<Integer> winning = new ArrayList<>();
    ArrayList<Integer> have = new ArrayList<>(8);
    int id;

    public int getPoints() {
        int p = 1;
        for (int i : winning) {
            if (have.contains(i)) {
                p *= 2;
            }
        }

        return p / 2;
    }

    public int getPointsForPartTwo() {
        int winningNumbers = getWinningNumbers();
        int c = 1;
        for (int i = 1; i <= winningNumbers; i++) {
            Card cardCopy = Day04.cards[id + i];
            c += cardCopy.getPointsForPartTwo();
        }

        return c;
    }

    public int getWinningNumbers() {
        int c = 0;
        for (int i : winning) {
            if (have.contains(i)) {
                c += 1;
            }
        }
        return c;
    }

}
