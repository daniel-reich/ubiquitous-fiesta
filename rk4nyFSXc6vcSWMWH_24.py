
def shared_digits(lst):
  for i in zip(lst, lst[1:]):
    y = False
    for j in str(i[0]):
      if j in str(i[1]):
        y = True
    if not y:
      return False
  return True

