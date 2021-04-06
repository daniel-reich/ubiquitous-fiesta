
def is_palindrome(p):
  p = ''.join([i.lower() for i in p if i.isalpha()])
  if len(p)<=1:
    return True
  elif p[0]!=p[-1]:
    return False
  return is_palindrome(p[1:-1])

