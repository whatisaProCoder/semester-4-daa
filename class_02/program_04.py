# Insert an element at n-th position in an array

arr = list(map(int, input("Enter the array : ").split()))
size = len(arr)

n = int(input("Enter position of element : "))
num = int(input("Enter the element : "))

if n > size or n <= 0:
  print("Invalid position")
  exit()

arr.append(0)
size += 1

i = size - 2
while i >= n:
    arr[i + 1] = arr[i]
    i -= 1

arr[n] = num

print("Final Array :-")
for i in range(size):
  print(arr[i], end=" ")