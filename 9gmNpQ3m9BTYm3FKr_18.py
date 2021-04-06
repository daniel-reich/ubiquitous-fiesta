
def lucky_seven(lst):
  check = 0
  if len(lst) < 3:
    return False
  else: 
    for a in lst:
      for b in lst:
        for c in lst:
          if a + b + c == 7 and a != b and a != c and b != c:
            check = 1
  if check == 1:
    return True
  else:
    return False

