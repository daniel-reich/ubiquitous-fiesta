
def is_alpha(word):
  return sum([ord(i) - 96 for i in word if i.isalpha()]) % 2 == 0

