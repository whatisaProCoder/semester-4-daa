# Binary Search Recursive

def binary_search(arr, key, l, r):  # O(1)
  if l > r:  # O(1) - base case
    return -1  # O(1)
  
  mid = l + (r - l) // 2  # O(1)
  
  if arr[mid] == key:  # O(1)
    return mid  # O(1)
  elif arr[mid] > key:  # O(1)
    return binary_search(arr, key, l, mid - 1)  # O(log n) - recursive call
  else:  # O(1)
    return binary_search(arr, key, mid + 1, r)  # O(log n) - recursive call

arr = list(map(int, input("Enter the array : ").split()))  # O(n) - n is array size

key = int(input("Enter target: "))  # O(1)

index = binary_search(arr, key, 0, len(arr) - 1)  # O(log n)

if index != -1:  # O(1)
  print(f"{key} is found at index : {index}")  # O(1)
else:  # O(1)
  print(f"{key} not found")  # O(1)

"""
RECURRENCE RELATION (Recursive Binary Search):
Let T(n) be the time to search in a sorted array of size n.
Each step does a constant amount of work (compute mid + 1 comparison)
and reduces the problem size to n/2:

  T(n) = T(n/2) + c,  for n > 1
  Base: T(1) = c

SUBSTITUTION (EXPANSION) METHOD:
Expand the recurrence k times:
  T(n) = T(n/2) + c
       = T(n/4) + 2c
       = T(n/8) + 3c
       = ...
After k expansions:
  T(n) = T(n/2^k) + k·c

Stop when the base case is reached:
  n/2^k = 1  ⇒  k = log₂ n

Substitute back:
  T(n) = T(1) + c·log₂ n = O(log n)

Space (recursive call stack): depth is log₂ n ⇒ O(log n).
"""