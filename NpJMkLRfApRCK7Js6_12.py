
def is_palindrome(wrd):
  return True if not wrd else is_palindrome(wrd[1:-1]) if wrd[0] == wrd[-1] else False

