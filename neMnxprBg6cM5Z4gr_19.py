
def arithmetic_progression(start, diff, n):
  ap_lst = []
  i = 0
  num = start
  while i < n:
    ap_lst.append(str(num))
    num += diff
    i += 1
  return ", ".join(ap_lst)

