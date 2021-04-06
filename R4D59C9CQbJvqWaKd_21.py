
def batting_avg(lst):
  return '{0:.3f}'.format(round(sum(x[0] for x in lst)/sum(x[1] \
  for x in lst),3))[1:]

