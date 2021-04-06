
def batting_avg(lst):
  res = round(sum([i[0] for i in lst]) / sum([i[1] for i in lst]), 3)
  return str(res)[1:].ljust(4, '0')

