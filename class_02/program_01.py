# Reverse a 'n' digit number

def reverse_number(n):  
  rev = 0  # 1
  while n > 0:  # (d+1)
    d = n % 10  # d
    rev = rev * 10 + d  # d
    n = n // 10  # d
  return rev  # 1

num = int(input("Enter number: "))  # 1

rev = reverse_number(num)  # 1

print(f"Reversed number: {rev}")  # 1
    