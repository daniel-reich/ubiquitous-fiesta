
def daily_streak(lst):
  idx = lst.index(False)
  a = lst[:idx].count(True)
  b = lst[idx + 1:].count(True)
  return (a if a >= b else b if b > a else 0)

