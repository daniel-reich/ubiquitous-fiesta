
def is_good_match(lst):
  if len(lst) % 2 == 1:
    return "bad match"
  else:
    arr = []
    i = 0
    while i < len(lst):
      arr.append(lst[i] + lst[i+1])
      i += 2
    return arr

