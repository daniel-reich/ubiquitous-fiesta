
def almost_palindrome(txt):
  half = int(len(txt)/2)
  print(half)
  wrong = 0
  for x in range(half):
    if txt[x] != txt[(len(txt) - 1) - x]:
      print("hit the if statement")
      wrong += 1
  print(wrong)
  if wrong == 1:
    return True
  else:
    return False

