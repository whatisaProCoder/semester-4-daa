"""
Matrix Multiplication (square matrices, standard algorithm)

Iterative (triple-loop) analysis:
  Work = ∑_{i=1}^n ∑_{j=1}^n ∑_{k=1}^n 1 = n^3 ⇒ T(n) = O(n^3)
  Space (result matrix): O(n^2)

Divide-and-Conquer Recurrence (optional analysis):
  Split matrices into 4 submatrices of size n/2.
  T(n) = 8 T(n/2) + c·n^2
Substitution (level expansion):
  After i levels: number of subproblems = 8^i, subproblem size = n/2^i
  Per-level non-recursive work = 8^i · c·(n/2^i)^2 = c·n^2 · 2^i
  Sum over i = 0..log₂ n - 1:
    c·n^2 · ∑_{i=0}^{log₂ n - 1} 2^i = c·n^2 (2^{log₂ n} - 1) = c·n^2 (n - 1) = O(n^3)
  Leaves contribute: 8^{log₂ n} · T(1) = n^{log₂ 8} · T(1) = n^3 · T(1) ⇒ O(n^3)
Thus, T(n) = O(n^3).
"""

from typing import List


def multiply_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
  n = len(A)
  C = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      s = 0
      for k in range(n):
        s += A[i][k] * B[k][j]
      C[i][j] = s
  return C


def read_matrix(n: int, name: str) -> List[List[int]]:
  print(f"Enter matrix {name} ({n} rows, space-separated):")
  M: List[List[int]] = []
  for _ in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
      raise ValueError("Row length must equal n for a square matrix")
    M.append(row)
  return M


def main() -> None:
  n = int(input("Enter n (matrix dimension): "))
  A = read_matrix(n, 'A')
  B = read_matrix(n, 'B')
  C = multiply_matrices(A, B)
  print("Product matrix C:")
  for row in C:
    print(*row)


if __name__ == "__main__":
  main()
