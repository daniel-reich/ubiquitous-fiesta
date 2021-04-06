
def divisible_by_left(n):
  return [False]+[False if v=='0' else int(n)%int(v)==0 \
  for n,v in zip(list(str(n))[1:],list(str(n)))]

