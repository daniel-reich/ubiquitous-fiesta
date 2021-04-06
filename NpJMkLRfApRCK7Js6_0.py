
def is_palindrome(wrd):
  return wrd == "" or (wrd[0] == wrd[-1] and is_palindrome(wrd[1:-1]))

