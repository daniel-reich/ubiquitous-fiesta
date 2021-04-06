
def is_palindrome(w):
  if len(w) <= 1:
    return True
  elif w[0] == w[-1]:
    return is_palindrome(w[1:-1])
  else:
    return False

