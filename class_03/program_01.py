# Binary Search

def binary_search(arr, key):  # O(1)
  l = 0  # O(1)
  r = len(arr)  # O(1)
  while l <= r:  # O(log n) - loop runs log n times
    mid = l + (r-l) // 2  # O(1)
    if arr[mid] == key:  # O(1)
      return mid  # O(1)
    elif arr[mid] > key:  # O(1)
      r = mid - 1  # O(1)
    else:  # O(1)
      l = mid + 1  # O(1)
  return -1  # O(1)

arr = list(map(int, input("Enter the array : ").split()))  # O(n) - n is array size

key = int(input("Enter target: "))  # O(1)

index = binary_search(arr, key)  # O(log n)

if index != -1:  # O(1)
  print(f"{key} is found at index : {index}")  # O(1)
else:  # O(1)
  print(f"{key} not found")  # O(1)


"""
RECURRENCE RELATION:
For Binary Search, the problem size is divided by 2 at each step.
T(n) = T(n/2) + c
where:
  - T(n) is the time complexity for input size n
  - T(n/2) represents the recursive call on half the array
  - c is the constant time for comparison and division operations
  
Base case: T(1) = c (when array has only 1 element)

SUBSTITUTION METHOD:
Let's solve T(n) = T(n/2) + c

Step 1: Expand the recurrence
T(n) = T(n/2) + c
     = [T(n/4) + c] + c = T(n/4) + 2c
     = [T(n/8) + c] + 2c = T(n/8) + 3c
     = [T(n/16) + c] + 3c = T(n/16) + 4c

Step 2: Identify the pattern
After k iterations: T(n) = T(n/2^k) + k*c

Step 3: Find when base case is reached
Base case is T(1), so: n/2^k = 1
                       n = 2^k
                       k = log₂(n)

Step 4: Substitute back
T(n) = T(1) + log₂(n) * c
     = c + c*log₂(n)
     = c(1 + log₂(n))

Step 5: Final complexity
T(n) = O(log n)

Therefore, Binary Search has logarithmic time complexity O(log n).
"""
