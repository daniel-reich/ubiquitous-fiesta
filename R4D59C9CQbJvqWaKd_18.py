
def batting_avg(lst):
  s=list(map(sum,zip(*lst)))
  return "{:.3f}".format(s[0]/s[-1])[1:]

