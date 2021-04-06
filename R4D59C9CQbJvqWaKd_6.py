
def batting_avg(lst):
  x = str(round(sum(i[0] for i in lst)/sum(i[1] for i in lst),3))[1:]
  if len(x) != 4:
    x += '0'*(4 - len(x))
  return x

