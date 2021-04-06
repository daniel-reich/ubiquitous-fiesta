
def is_alpha(word):
  return sum(ord(x)-96 for x in word if x.isalpha())%2==0

