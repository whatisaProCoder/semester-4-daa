package program_01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class KnapsackDP {

  private static int[][] buildDpTable(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];

    for (int i = 1; i <= n; i++) {
      int currentWeight = weights[i - 1];
      int currentValue = values[i - 1];

      for (int w = 0; w <= capacity; w++) {
        dp[i][w] = dp[i - 1][w];
        if (currentWeight <= w) {
          dp[i][w] = Math.max(dp[i][w], currentValue + dp[i - 1][w - currentWeight]);
        }
      }
    }

    return dp;
  }

  private static List<Integer> getSelectedItems(int[] weights, int[] values, int capacity, int[][] dp) {
    List<Integer> selected = new ArrayList<>();
    int i = weights.length;
    int w = capacity;

    while (i > 0 && w >= 0) {
      if (dp[i][w] != dp[i - 1][w]) {
        selected.add(i - 1);
        w -= weights[i - 1];
      }
      i--;
    }

    Collections.reverse(selected);
    return selected;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter number of items: ");
    int n = scanner.nextInt();

    int[] weights = new int[n];
    int[] values = new int[n];

    System.out.println("Enter weights of items:");
    for (int i = 0; i < n; i++) {
      weights[i] = scanner.nextInt();
    }

    System.out.println("Enter values of items:");
    for (int i = 0; i < n; i++) {
      values[i] = scanner.nextInt();
    }

    System.out.print("Enter knapsack capacity: ");
    int capacity = scanner.nextInt();

    int[][] dp = buildDpTable(weights, values, capacity);
    int maxValue = dp[n][capacity];
    List<Integer> selectedItems = getSelectedItems(weights, values, capacity, dp);

    System.out.println("Maximum value = " + maxValue);
    System.out.println("Selected item indices (0-based): " + selectedItems);

    scanner.close();
  }
}
