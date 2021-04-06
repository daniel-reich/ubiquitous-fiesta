
def same_line(lst):
  try:
    return (lst[1][1] - lst[0][1]) / (lst[1][0] - lst[0][0]) == (lst[2][1] - lst[1][1]) / (lst[2][0] - lst[1][0])
  except:
    return lst[0][0] == 0 and lst[1][0] == 0 and lst[2][0] == 0

