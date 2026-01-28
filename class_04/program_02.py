"""
Merge Sort

Recurrence:
  T(n) = 2 T(n/2) + c·n,  for n > 1
  T(1) = c
(Subproblems are halves; merging costs linear time.)

Substitution (expansion) method:
  T(n) = 2[ T(n/4) + c·(n/2) ] + c·n = 4 T(n/4) + 2c·n + c·n = 4 T(n/4) + 3c·n
  After i steps: T(n) = 2^i T(n/2^i) + i·c·n
  Stop when n/2^i = 1 ⇒ i = log₂ n
  T(n) = n·T(1) + c·n·log₂ n = O(n log n)

Space: O(n) auxiliary for merging (not in-place).
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
  i = j = 0
  out: List[int] = []
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      out.append(left[i])
      i += 1
    else:
      out.append(right[j])
      j += 1
  if i < len(left):
    out.extend(left[i:])
  if j < len(right):
    out.extend(right[j:])
  return out


def merge_sort(arr: List[int]) -> List[int]:
  n = len(arr)
  if n <= 1:
    return arr
  mid = n // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left, right)


def main() -> None:
  arr = list(map(int, input("Enter the array: ").split()))
  sorted_arr = merge_sort(arr)
  print("Sorted Array:", *sorted_arr)


if __name__ == "__main__":
  main()
