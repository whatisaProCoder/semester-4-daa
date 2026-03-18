#include <stdio.h>
#include <stdlib.h>

#define MAX 10

// Function to multiply two matrices
void multiply(int a[MAX][MAX], int b[MAX][MAX], int result[MAX][MAX], int r1,
              int c1, int r2, int c2) {
  int i, j, k;

  for (i = 0; i < r1; i++) {
    for (j = 0; j < c2; j++) {
      result[i][j] = 0;
      for (k = 0; k < c1; k++) {
        result[i][j] += a[i][k] * b[k][j];
      }
    }
  }
}

int main() {
  int n;
  int matrices[10][MAX][MAX];
  int rows[10], cols[10];
  int result[MAX][MAX];
  int temp[MAX][MAX];

  printf("Enter number of matrices: ");
  scanf("%d", &n);

  if (n < 2) {
    printf("Need at least 2 matrices for multiplication.\n");
    return 0;
  }

  // Input matrices
  for (int m = 0; m < n; m++) {
    printf("\nMatrix %d\n", m + 1);
    printf("Enter rows and columns: ");
    scanf("%d %d", &rows[m], &cols[m]);

    printf("Enter elements:\n");
    for (int i = 0; i < rows[m]; i++) {
      for (int j = 0; j < cols[m]; j++) {
        scanf("%d", &matrices[m][i][j]);
      }
    }
  }

  // Check compatibility
  for (int i = 0; i < n - 1; i++) {
    if (cols[i] != rows[i + 1]) {
      printf("Matrix multiplication not possible.\n");
      return 0;
    }
  }

  // Copy first matrix to temp
  for (int i = 0; i < rows[0]; i++) {
    for (int j = 0; j < cols[0]; j++) {
      temp[i][j] = matrices[0][i][j];
    }
  }

  int r = rows[0];
  int c = cols[0];

  // Multiply sequentially
  for (int m = 1; m < n; m++) {
    multiply(temp, matrices[m], result, r, c, rows[m], cols[m]);

    r = r;        // rows remain same
    c = cols[m];  // columns update

    // Copy result back to temp
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        temp[i][j] = result[i][j];
      }
    }
  }

  // Display final result
  printf("\nFinal Result Matrix:\n");
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      printf("%d ", temp[i][j]);
    }
    printf("\n");
  }

  return 0;
}
