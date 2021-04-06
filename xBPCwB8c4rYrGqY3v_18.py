
def missing(lst):
  diff = min([abs(lst[i]-lst[i+1]) for i in range(len(lst)-1)])
  return [x for x in [x+diff for x in lst[:-1]] if x not in lst][0]

