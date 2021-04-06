
def ranged_reversal(lst, start, finish):
  return (
    lst[0:start] +
    lst[start:finish+1][::-1] +
    lst[finish+1:]
  )

