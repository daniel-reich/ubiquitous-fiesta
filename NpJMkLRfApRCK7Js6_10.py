
def is_palindrome(wrd, i=0):
  return wrd[i]==wrd[-i-1] and is_palindrome(wrd, i+1) if i<len(wrd) else 1

