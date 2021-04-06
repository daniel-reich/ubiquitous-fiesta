
def break_point(num):
  ns = [int(d) for d in str(num)]
  sums = [0]
  for d in ns: sums+= [sums[-1]+d]
  return sums[-1]/2 in sums

