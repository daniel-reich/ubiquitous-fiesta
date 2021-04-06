
def ranged_reversal(lst, start, finish):
  if (start - finish) == 0:
    return lst
  elif start == 0 and finish == (len(lst) - 1):
    return lst[::-1]
  elif start == 0:
    return lst[finish::-1] + lst[(finish + 1):]
  elif finish == 0:
    return lst[:start] + lst[:(start - 1):-1]
  else:
    return lst[:start] + lst[finish: (start - 1): -1] + lst[finish+1:]

