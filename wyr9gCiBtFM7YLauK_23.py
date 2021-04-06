
def time_sum(times):
  lst = [tuple(map(int, t.split(':'))) for t in times]
  h = m = s = 0
  for time in lst:
    h += time[0]
    m += time[1]
    s += time[2]
  h += m//60
  m = m%60 + s//60
  s = s%60
  return [h, m, s]

