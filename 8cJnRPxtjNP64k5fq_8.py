
def dance(lst,p):
  return [[n[0], r[1]] if p == 'men' else [r[0], n[1]] for n, r in zip(lst, lst[::-1])]

