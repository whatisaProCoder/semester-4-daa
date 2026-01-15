# Delete the n-th element from an array of 'm' no.s

arr = list(map(int, input("Enter the array : ").split()))  # 1
size = len(arr)  # 1

n = int(input("Enter position of element : "))  # 1

if n > size:  # 1
  print("Invalid position")  # 0 or 1

for i in range(n, size, 1):  # (m-n+1)
  arr[i-1]=arr[i]  # (m-n)

size -= 1  # 1

print("Final Array :-")  # 1
for i in range(size):  # (m)
  print(arr[i], end=" ")  # (m-1)