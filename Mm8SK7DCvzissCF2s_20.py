
def is_alpha(word):
  return sum(ord(l)- 96 for l in word if l.isalpha())%2 == 0

