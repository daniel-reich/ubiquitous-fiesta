
def first_before_second(s, first, second):
  secFound = False
  for let in s:
    if secFound==True and let==first:
      return False
    elif let==second:
      secFound = True
  return True

