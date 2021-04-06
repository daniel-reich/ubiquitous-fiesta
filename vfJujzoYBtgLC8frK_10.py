
def word_to_decimal(word):
  word = word.upper()
  b = 10 + max(ord(l)-64 for l in word)
  return sum((9+ord(l)-64)*b**i for i,l in enumerate(word[::-1]))

