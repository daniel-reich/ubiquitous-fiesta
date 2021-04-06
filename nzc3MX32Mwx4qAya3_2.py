
def ranged_reversal(lst, start, finish):
  lst[start:finish+1]=lst[start:finish+1][::-1]
  return lst

