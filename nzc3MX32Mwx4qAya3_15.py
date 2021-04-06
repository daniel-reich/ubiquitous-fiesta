
def ranged_reversal(lst, start, finish):
  a = lst[:start]
  b = lst[start:finish+1]
  c = lst[finish+1:]
  if len(lst) == len(list(range(start,finish+1))):
    return lst[::-1]
  else:
    return a + b[::-1] + c

