import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;

public class Day03 {

    private static char[][] array;
    final static int SIZE = 140;

    public static void main(String[] args) throws IOException {

        File file = new File("src/main/java/de/halberfan/adventofcode/y2023/day03/input.txt");
        FileReader fileReader = new FileReader(file);
        BufferedReader reader = new BufferedReader(fileReader);

        String st;
        array = new char[SIZE][SIZE];
        int count = 0;
        while ((st = reader.readLine()) != null) {
            int count2 = 0;
            for (char c : st.toCharArray()) {
                array[count][count2++] = c;
            }
            count++;
        }

        partOne();
        partTwo();

    }

    public static void partOne() {

        ArrayList<Num> numbers = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {

                char c = array[i][j];
                boolean isSymbol = isSymbol(c);

                if (!isSymbol) {
                    continue;
                }

                for (int a = -1; a < 2; a++) {
                    for (int b = -1; b < 2; b++) {
                        char l = array[i + a][j + b];
                        if(isNumber(l)) {
                            Num n = findNumberFromArrayByCoordinates(i+a,j+b);
                            if(!numbers.contains(n)) {
                                numbers.add(n);
                            }
                        }
                    }
                }

            }
        }


        System.out.println(sumFromArrayList(numbers));

    }

    public static void partTwo() {

        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {

                char c = array[i][j];

                if (c != '*') {
                    continue;
                }

                ArrayList<Num> partNumbers = new ArrayList<>(2);

                for (int a = -1; a < 2; a++) {
                    for (int b = -1; b < 2; b++) {
                        char l = array[i + a][j + b];
                        if(isNumber(l)) {
                            Num n = findNumberFromArrayByCoordinates(i+a,j+b);
                            if(!contains(partNumbers, n)) {
                                partNumbers.add(n);
                            }
                        }
                    }
                }

                if(partNumbers.size() == 2) {

                    int ratio = partNumbers.get(0).n * partNumbers.get(1).n;
                    numbers.add(ratio);
                    System.out.println(partNumbers);
                }

            }
        }


        System.out.println(sumFromIntArrayList(numbers));

    }

    private static boolean contains(ArrayList a, Object b) {
        for (Object o : a) {
            if (o.equals(b))
                return true;
        }
        return false;
    }


    private static boolean isSymbol(char c) {
        String s = String.valueOf(c);
        return !s.matches("[0-9.]");
    }

    private static boolean isNumber(char c) {
        String s = String.valueOf(c);
        return s.matches("[0-9]");
    }

    private static Num findNumberFromArrayByCoordinates(int x, int y) {

        StringBuilder s = new StringBuilder();

        s.append(array[x][y]);

        int b = y + 1;
        while (b != SIZE && isNumber(array[x][b])) {
            s.append(array[x][b]);
            b++;
        }
        b = y - 1;
        while (b != -1 && isNumber(array[x][b])) {
            s.insert(0, array[x][b]);
            b--;
        }

        int n = Integer.parseInt(s.toString());
        return new Num(n, x, b + 1);
    }

    private static int sumFromArrayList(ArrayList<Num> arrayList) {
        int s = 0;
        for (Num a : arrayList) {
            int i = a.n;
            s += i;
        }
        return s;
    }

    private static int sumFromIntArrayList(ArrayList<Integer> arrayList) {
        int s = 0;
        for (Integer i : arrayList) {
            s += i;
        }
        return s;
    }

}

class Num {

    int n;
    int x, y;

    public Num(int n, int x, int y) {
        this.n = n;
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Num num = (Num) o;
        return x == num.x && y == num.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public String toString() {
        return "Num{" +
                "n=" + n +
                ", x=" + x +
                ", y=" + y +
                '}';
    }
}
