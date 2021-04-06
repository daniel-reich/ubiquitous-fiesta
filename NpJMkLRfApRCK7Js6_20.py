
def is_palindrome(wrd):
  return len(wrd) <= 1 or (wrd[0] == wrd[-1] and is_palindrome(wrd[1:-1]))

