
def count_digits(lst, t):
  f={"odd":lambda x:int(x)%2, "even":lambda x:1-int(x)%2}
  return [sum(map(f[t],list(str(i)))) for i in lst]

