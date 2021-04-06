
def is_palindrome(wrd):
  if len(wrd) < 2:
    return True
  if wrd[0] != wrd[-1]:
    return False
  return is_palindrome(wrd[1:-1])

