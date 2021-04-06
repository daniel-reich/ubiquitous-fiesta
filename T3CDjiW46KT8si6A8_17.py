
def product(lst):
  return sorted(set(lst))[-2]*sorted(set(lst))[-1] if len(set(lst))>1 else sorted(set(lst))[-1]*sorted(set(lst))[-1]

