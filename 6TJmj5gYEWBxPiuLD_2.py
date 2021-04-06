
def seating_students(lst):
  def loop(fr, to, step):
    res = 0
    for i in range(fr, to, 2):
      if not (i in lst or i+step in lst):
        res += 1
    return res
  n = lst.pop(0)
  return loop(1, n-2, 2) + loop(2, n, 2) + loop(1, n, 1)

