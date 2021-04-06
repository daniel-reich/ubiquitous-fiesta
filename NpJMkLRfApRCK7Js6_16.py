
def is_palindrome(wrd):
  # your recursive solution here
  if len(wrd) <= 1:
    return True
  if wrd[0] != wrd[-1]:
    return False
  return is_palindrome(wrd[1:-1])

