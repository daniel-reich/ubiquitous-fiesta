
def list_of_multiples (num, length):
  list = []
  multi = 0
  finish = None
  while not finish:
    multi = multi + 1
    list.append(num*multi)
    if multi == length:
      finish = True
  return list

