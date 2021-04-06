
def is_palindrome(wrd):
  if len(wrd) == 1:
    return True
  else:
    return is_palindrome(wrd[1:-1]) if wrd[0] == wrd[-1] else False

