
def cup_swapping(lst):
  cups_lst = [0, 1, 0]
  for txt in lst:
    a = ord(txt[0]) - 65
    b = ord(txt[1]) - 65
    cups_lst[a], cups_lst[b] = cups_lst[b], cups_lst[a]
  return "ABC"[cups_lst.index(1)]

