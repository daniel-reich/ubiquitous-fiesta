
def combine(lst):
  return {a[0]: [a[2], b[2]] for a, b in zip(lst[::2], lst[1::2])}

