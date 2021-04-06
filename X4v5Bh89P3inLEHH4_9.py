
def spin_around(lst):
  deg_lst = []
  for item in lst:
    if item == "right":
      deg_lst.append(90)
    else:
      deg_lst.append(-90)
  result = abs(sum(deg_lst))
  ans = result//360
  return ans

