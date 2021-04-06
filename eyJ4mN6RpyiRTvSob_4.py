
def is_palindrome_possible(txt):
  oddcount=0
  for char in txt:
    if txt.count(char)%2 != 0:
      oddcount+=1/txt.count(char)
  if oddcount>1:
    return False
  else:
    return True

