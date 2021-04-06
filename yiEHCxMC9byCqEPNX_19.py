
def is_palindrome(p):
  if not p:
    return True
  elif not p[0].isalpha():
    return is_palindrome(p[1:])
  elif not p[-1].isalpha():
    return is_palindrome(p[:-1])
  elif p[0].lower()==p[-1].lower():
    return is_palindrome(p[1:-1])
  return False

