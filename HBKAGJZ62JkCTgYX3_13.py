
def last(a, n):
  if n> len(a):
    return 'invalid'
  else:
    return [a[i] for i in range(-n,0)]

