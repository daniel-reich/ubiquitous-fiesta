
def is_repdigit(num):
  try:
    lst=[int(x) for x in str(num)]
    if num < 0:
      return False
    if num == 0:
      return True
    for i in lst:
      if lst.count(i) == len(lst):
        return True
    else: return False
  except : return False

