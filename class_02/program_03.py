# Delete the n-th element from an array of 'm' no.s

arr = list(map(int, input("Enter the array : ").split()))
size = len(arr)

n = int(input("Enter position of element : "))

if n > size:
  print("Invalid position")

for i in range(n, size, 1):
  arr[i-1]=arr[i]

size -= 1

print("Final Array :-")
for i in range(size):
  print(arr[i], end=" ")