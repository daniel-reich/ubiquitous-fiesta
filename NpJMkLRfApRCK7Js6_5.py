
def is_palindrome(wrd):
  if len(wrd) <= 1:
    return True
  if wrd[0] != wrd[-1]:
    return False
  return is_palindrome(wrd[1:len(wrd)-1])

