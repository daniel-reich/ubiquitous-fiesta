
def is_palindrome(p):
  p = "".join([let.lower() for let in p if let.isalpha()])
  if len(p) < 2:
    return True
  if p[0] != p[-1]:
    return False
  return is_palindrome(p[1:-1])

