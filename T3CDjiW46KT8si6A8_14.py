
def product(lst):
  if len(set(lst)) == 1:  return lst[0]**2
  return sorted(lst)[-1] * sorted(set((lst)))[-2]

