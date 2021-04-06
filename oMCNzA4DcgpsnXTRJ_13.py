
def missing_num(lst):
  return [i for i in sorted(range(1, 10 + 1)) if not i in lst][0]

