
def combine(lst):
  return {x[0]: [x[-1], y[-1]] for x, y in zip(lst[:-1:2], lst[1::2])}

