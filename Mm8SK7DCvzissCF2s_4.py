
def in_alpha(word):
  return sum(ord(l.lower())-96 for l in word if l.isalpha())%2 == 0

