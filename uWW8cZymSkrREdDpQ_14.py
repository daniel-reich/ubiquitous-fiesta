
def find_in_list(lst, el, start = 0):
  for i in range(start, len(lst)):
    if lst[i] == el: return i
  return -1
​
def sums_up(lst):
  pairs = []
  ix = 0
  while ix < len(lst) - 1:
    if lst[ix] != None:
      ip = find_in_list(lst, 8-lst[ix], ix+1)
      if ip >= 0:
        pairs.append((ip, sorted([lst[ix], lst[ip]])))
        lst[ip] = None
    ix += 1
  return {"pairs": [t[1] for t in sorted(pairs, key=lambda el: el[0])]}

