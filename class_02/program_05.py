# Find the no. of words in a given sentence

sentence = input("Enter sentence :-\n")  # 1
num_words = 0  # 1

if sentence != "":  # 1
  num_words += 1  # 0 or 1

for ch in sentence:  # (n+1)
  if ch == " ":  # n
    num_words += 1  # 0 to n

print(f"Number of words : {num_words}")  # 1