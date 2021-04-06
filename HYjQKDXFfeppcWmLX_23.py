
def is_curzon(num):
  numb1 = 2 ** num + 1
  numb2 = 2 * num + 1
  if (numb1%numb2 == 0):
    return True
  else :
    return False

