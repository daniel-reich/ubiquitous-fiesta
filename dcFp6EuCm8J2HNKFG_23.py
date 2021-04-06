
def func(lst):
  global count
  count=0
  def recur(lst):
    global count
    for i in lst:
      if isinstance(i, list):
        count += 1
        recur(i)
      else: count += 1
    return count
  return recur(lst)

