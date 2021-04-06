
vowels = {"A":4, "E":3, "I":1}
​
def sum_of_vowels(sentence):
  total = 0
  for char in sentence.upper():
    if char in vowels:
      total += vowels[char]
  return total

