# Insert an element at n-th position in an array

arr = list(map(int, input("Enter the array : ").split()))  # 1
size = len(arr)  # 1

n = int(input("Enter position of element : "))  # 1
num = int(input("Enter the element : "))  # 1

if n > size or n <= 0:  # 1
  print("Invalid position")  # 0 or 1
  exit()  # 0 or 1

arr.append(0)  # 1
size += 1  # 1

i = size - 2  # 1
while i >= n:  # (size-n)
    arr[i + 1] = arr[i]  # (size-n-1)
    i -= 1  # (size-n-1)

arr[n] = num  # 1

print("Final Array :-")  # 1
for i in range(size):  # (size+1)
  print(arr[i], end=" ")  # size