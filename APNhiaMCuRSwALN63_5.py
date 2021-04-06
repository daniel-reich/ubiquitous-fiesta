
def almost_palindrome(txt):
  slice = int(round(len(txt)/2,0))
  return sum([(x!=y) for x,y in zip(txt[:slice],txt[:-slice-1:-1])]) == 1

