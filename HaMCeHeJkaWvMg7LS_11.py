
def sun_loungers(beach):
  beach = list(beach)
  if len(beach) < 2:
    return 1 if beach == ['0'] else 0
  if beach[0] == beach[1] == '0':
    beach[0] = 2
  for i in range(1,len(beach)-1):
    if beach[i] == '0' and beach[i-1] == '0' and beach[i+1] == '0':
      beach[i] = 2
  if beach[-2] == beach[-1] == '0':
    beach[-1] = 2
  return beach.count(2)

