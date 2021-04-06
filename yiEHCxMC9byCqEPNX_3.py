
def is_palindrome(p):
  if not p: return True
  else: p = ''.join([x.lower() for x in p if x.isalpha()])
  if p[0] == p[-1]:return is_palindrome(p[1:-1])
  else: return False

