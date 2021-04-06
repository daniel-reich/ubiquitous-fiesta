
def is_good_match(lst):
  if len(lst) % 2 != 0:
    return "bad match"
  l = []
  for i in range(0, len(lst), 2):
    l.append(lst[i] + lst[i+1])
  return l

