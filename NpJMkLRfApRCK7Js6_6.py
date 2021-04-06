
def is_palindrome(wrd, n=1):
  if wrd[n - 1] != wrd[-n]:
    return False
  return is_palindrome(wrd, n + 1) if n < len(wrd) else True

