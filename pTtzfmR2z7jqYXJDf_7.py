
def possible_palindrome(txt):
  oneOdd = False
  if len(set(txt)) == 1:
    return True
  if len(txt) %2:
    for letter in txt:
      if txt.count(letter) % 2:
        if oneOdd == True:
          return False
        else:
          oneOdd = True
  else:
    for letter in txt:
      if txt.count(letter) % 2:
        return False
  
  return True

