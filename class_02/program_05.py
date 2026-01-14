# Find the no. of words in a given sentence

sentence = input("Enter sentence :-\n")
num_words = 0

if sentence != "":
  num_words += 1

for ch in sentence:
  if ch == " ":
    num_words += 1

print(f"Number of words : {num_words}")