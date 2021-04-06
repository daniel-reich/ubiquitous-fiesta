
def ranged_reversal(lst, start, finish):
  x=lst[:start]
  y=lst[start:finish+1]
  z=lst[finish+1:]
  return x+y[::-1]+z

