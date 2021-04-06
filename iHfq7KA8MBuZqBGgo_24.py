
def is_legitimate(lst):
  f_l = all([j == 0 for i in lst for j in i if i == lst[0] or i == lst[-1]])
  sides = all([i[0] == 0 and i[-1] == 0 for i in lst[1:-1]])
  return sides and f_l

