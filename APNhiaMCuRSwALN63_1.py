
def almost_palindrome(txt):
  return sum(1 for i in range(len(txt)) if txt[i] != txt[-1-i]) == 2

