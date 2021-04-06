
def is_symmetrical(num):
  lst = list(str(num))
  rlst = list(reversed(lst))
  reversednum = "".join(rlst)
  if num == int(reversednum):
    return True
  else:
    return False

