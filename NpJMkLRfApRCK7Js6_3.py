
def is_palindrome(wrd):
  if len(wrd)<2:
    return True
  return wrd[0]==wrd[-1] and is_palindrome(wrd[1:-1])

