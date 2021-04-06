
def ranged_reversal(lst, start, finish):
  temp = lst[start:finish+1]
  temp.reverse()
  return lst[:start] + temp + lst[finish+1:]

