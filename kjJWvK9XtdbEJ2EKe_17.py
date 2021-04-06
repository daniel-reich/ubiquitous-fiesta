
def sort_array(lst):
  a = []
  while True:
    if lst != []:
      a.append(min(lst))
      lst.remove(min(lst))
      continue
    else:
      break
  return a

