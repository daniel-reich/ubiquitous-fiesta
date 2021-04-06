
def product(lst):
  return sorted(set(lst))[-1] * sorted(set(lst))[-2] if len(set(lst)) > 1 else max(lst) ** 2

