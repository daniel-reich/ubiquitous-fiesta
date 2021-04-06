
def batting_avg(lst):
  hits = sum(i[0] for i in lst)
  at_bats = sum(i[1] for i in lst)
​
  return str(round(hits/at_bats, 3))[1:].ljust(4,'0')

