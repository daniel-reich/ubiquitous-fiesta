
def first_before_second(s, first, second):
  found_first= False
  found_second = False
  for letter in s:
    if not found_first:
      if letter == second:
        return False
      if(letter == first):
        found_first= True
    else:
      if not found_second:
        if(letter == second):
          found_second = True
      else:
        if(letter== first):
          return False;
  return True

