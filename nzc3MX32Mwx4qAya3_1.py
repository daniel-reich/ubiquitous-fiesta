
def ranged_reversal(lst, start, finish):
  beg = lst[:start]
  mid = lst[start:finish+1]
  end = lst[finish+1:]
​
  return beg + mid[::-1] + end

