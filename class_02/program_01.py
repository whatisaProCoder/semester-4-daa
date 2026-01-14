# Reverse a 'n' digit number

def reverse_number(n): # O(1+n+1+1)
  rev = 0 # O(1)
  while n > 0: # O(n)
    d = n % 10 # O(1)
    rev = rev * 10 + d # O(1)
    n = n // 10 # O(1)
  return rev

num = int(input("Enter number: "))

rev = reverse_number(num)

print(f"Reversed number: {rev}")

# Total time complexity : 1+n+1+1 = n
    