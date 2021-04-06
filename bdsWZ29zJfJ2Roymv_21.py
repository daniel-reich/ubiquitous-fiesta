
def swap_two(txt):
  lst = []
  for i in range(0, len(txt), 2):
    lst.append(txt[i:i+2])
  for i in range(1, len(lst), 2):
    if len(lst[i]) > 1:
      x = lst[i]
      y = lst[i-1]
      lst[i] = y
      lst[i-1] = x
  return "".join(lst)

