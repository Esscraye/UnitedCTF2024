/*
 * Decompiled with CFR 0.151.
 */
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Enter the serial number: ");
        Main.readSomething();
    }

    public static void readSomething() {
        Main.secretFunction();
    }

    public static void readAnotherThing() {
        System.out.println("Enter the password");
        Scanner scanner = new Scanner(System.in);
        Main.validatePassword(scanner.nextLine());
    }

    public static void secretFunction() {
        Main.whatEvenIsBase64();
        Main.readAnotherThing();
    }

    public static void whatEvenIsBase64() {
        Main.ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl();
    }

    public static void validatePassword(String pwd) {
        throw new RuntimeException("This software is outdated. Current version is 0.0.1\nMost recent version is 2.2.1");
    }

    public static String ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl() {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        System.out.println(String.valueOf(a));
        return "ZmxhZy1Eb250UHJpbnRUaGVTdGFja1RyYWNl";
    }
}

