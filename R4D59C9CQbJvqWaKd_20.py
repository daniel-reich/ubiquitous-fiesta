
def batting_avg(lst):
  hits = sum(e[0] for e in lst)
  bats = sum(e[-1] for e in lst)
​
  return "{:0.3f}".format(round(hits / bats, 3))[1:]

