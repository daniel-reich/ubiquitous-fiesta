
def find_fulcrum(lst):
  s = sum(lst)
  running = 0
  for i in lst:
    if running == (s-i)//2:
      return i
    running += i
  return -1

