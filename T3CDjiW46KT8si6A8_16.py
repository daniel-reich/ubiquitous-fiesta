
def product(lst):
  return sorted(set(lst))[-1] ** 2 if len(set(lst)) < 2 else sorted(set(lst))[-1] * sorted(set(lst))[-2]

