
def third_most_expensive(dct):
  lst = sorted(dct.values(), reverse=True)
  return False if len(lst) < 3 else [i for i in dct.keys() if dct[i] == lst[2]][0]

