
def same_line(lst):
  if lst[0][0] == lst[1][0] == lst[2][0]:
    return True
  else:
    if (lst[1][0]-lst[0][0]) == 0 or (lst[2][0]-lst[0][0]) == 0:
      return False
    else:
      if (lst[1][1]-lst[0][1])/(lst[1][0]-lst[0][0]) == (lst[2][1]-lst[0][1])/(lst[2][0]-lst[0][0]):
        return True
      else:
        return False

