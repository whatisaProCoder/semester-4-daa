# Selection Sort

n = int(input("Enter number of elements: "))

arr = []
print(f"Enter {n} elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    minIndex = i
    
    for j in range(i + 1, n):
        if arr[j] < arr[minIndex]:
            minIndex = j
    
    temp = arr[i]
    arr[i] = arr[minIndex]
    arr[minIndex] = temp

print("Sorted array:")
for i in range(n):
    print(arr[i], end=" ")
print()
