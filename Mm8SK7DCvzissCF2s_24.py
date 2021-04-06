
def in_alpha(word):
  return sum(ord(letter.lower()) - 96 for letter in word if letter.isalpha()) % 2 == 0

