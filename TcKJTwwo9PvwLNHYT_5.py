
def is_palindrome(txt):
  new = []
  for char in txt:
    new.append(char)
  
  if "".join(new[::-1]) == txt:
    return True
  else:
    return False

