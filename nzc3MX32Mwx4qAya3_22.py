
def ranged_reversal(lst, start, finish):
  return lst[:start] + list(reversed(lst[start:finish + 1])) + lst[finish + 1:]

