
def word_to_decimal(word):
  base = max([ord(i) - 96 for i in word.lower()]) + 10
  return sum((ord(j)-87) * base**i for i, j in enumerate(word.lower()[::-1]))

