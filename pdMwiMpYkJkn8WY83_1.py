
def is_palindrome(w):
  if len(w)<2:return 1
  if w[0]!=w[-1]:return 0
  return is_palindrome(w[1:-1])

