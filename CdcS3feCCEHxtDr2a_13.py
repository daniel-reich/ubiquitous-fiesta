
def clear_ordering(lst):
  start = []
  end = []
  for s, e in lst:
    start.append(s)
    end.append(e)
  return len(set(start)^set(end)) == 2

