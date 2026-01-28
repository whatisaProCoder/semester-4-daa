"""
Quick Sort

Recurrence (general):
  T(n) = T(k) + T(n-k-1) + c·n,  0 ≤ k ≤ n-1    (partition costs linear time)

Worst case (highly unbalanced, e.g., k = n-1):
  T(n) = T(n-1) + c·n
Substitution (expansion):
  T(n) = [T(n-2) + c(n-1)] + c n = T(n-2) + c(2n - 1)
  ... after i steps: T(n) = T(n-i) + c(i·n - (1+2+···+(i-1)))
  With i = n-1: T(n) = T(1) + Θ(n^2) ⇒ O(n^2)

Average/balanced case (assume roughly equal splits):
  T(n) = 2 T(n/2) + c·n
Substitution (expansion) method:
  T(n) = 2[ T(n/4) + c·(n/2) ] + c·n = 4 T(n/4) + 2c·n + c·n = 4 T(n/4) + 3c·n
  After i steps: T(n) = 2^i T(n/2^i) + i·c·n
  Stop when n/2^i = 1 ⇒ i = log₂ n
  T(n) = n·T(1) + c·n·log₂ n = O(n log n)

Space (recursion stack): average O(log n), worst O(n). In-place aside from recursion.
"""

from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


def quick_sort(arr: List[int], low: int, high: int) -> None:
  if low < high:
    p = partition(arr, low, high)
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)


def main() -> None:
  arr = list(map(int, input("Enter the array: ").split()))
  if arr:
    quick_sort(arr, 0, len(arr) - 1)
  print("Sorted Array:", *arr)


if __name__ == "__main__":
  main()
