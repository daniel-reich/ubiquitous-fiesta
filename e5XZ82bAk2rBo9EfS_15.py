
def bed_time(*args):
  times = []
  for x in args:
    wake,dur=[[int(n) for n in t.split(':')] for t in x]
    m=(wake[1]-dur[1])%60
    h=(wake[0]-dur[0])%24 - (1 if wake[1]<dur[1] else 0)
    times.append('{:0>2}:{:0>2}'.format(h,m))
  return times

