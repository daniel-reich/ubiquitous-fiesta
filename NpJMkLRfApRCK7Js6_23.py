
wrd = 'madam' 
def is_palindrome(wrd):
  # your recursive solution here
  
  #print(wrd)
  
  if len(wrd) == 1 or len(wrd) == 0:
    return True
  
  if wrd[0] == wrd[-1]:
    return is_palindrome(wrd[1:-1])
  else:
    return False

