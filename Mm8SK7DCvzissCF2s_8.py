
def in_alpha(word):
  x = [ord(i) - 96 for i in word if i.isalpha()]
  return sum(x) % 2 == 0

