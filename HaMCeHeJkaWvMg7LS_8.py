
def sun_loungers(beach):
  return sum(max(0, (len(s)-1)//2) for s in ('0'+beach+'0').split('1'))

