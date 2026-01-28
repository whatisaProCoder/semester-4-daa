# Bubble Sort

def bubble_sort(my_list):  # O(1)
  for i in range(len(my_list) - 1, 0, -1):  # O(n) - outer loop runs n times
    for j in range(i):  # O(n) - inner loop runs n times on average
      if my_list[j] > my_list[j+1]:  # O(1)
        temp = my_list[j]  # O(1)
        my_list[j] = my_list[j+1]  # O(1)
        my_list[j+1] = temp  # O(1)
  return my_list  # O(1)

my_list = list(map(int, input("Enter the array : ").split()))  # O(n)

my_list = bubble_sort(my_list)  # O(n^2)

print("Sorted Array :", end=" ")  # O(1)
print(my_list)  # O(n)

"""
RECURRENCE RELATION (Bubble Sort):
Let T(n) be the time to sort an array of size n.
Each outer pass bubbles the largest element to the end, doing (n-1)
adjacent comparisons/swaps, then reduces the effective problem size by 1:

  T(n) = T(n-1) + c·(n-1),  for n > 1
  Base: T(1) = c

SUBSTITUTION (EXPANSION) METHOD:
Expand the recurrence k times:
  T(n) = T(n-1) + c(n-1)
       = [T(n-2) + c(n-2)] + c(n-1)
       = T(n-2) + c[(n-2) + (n-1)]
       = ...
After k expansions:
  T(n) = T(n-k) + c · ∑_{i=n-k}^{n-1} i

Stop when the base case is reached (k = n-1):
  T(n) = T(1) + c · ∑_{i=1}^{n-1} i
       = T(1) + c · (n-1)n / 2

Therefore: T(n) = O(n^2)

Space: Bubble sort uses constant extra space ⇒ O(1).
"""