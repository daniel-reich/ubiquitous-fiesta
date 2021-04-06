
def sun_loungers(beach):
  c = 0
​
  if beach == '0':
    return 1
​
  if beach.startswith('00'):
    beach = '10' + beach[2:]
    c += 1
​
  for i in range(len(beach)):
    if beach[i-1:i+2] == '000':
      beach = beach[:i] + '1' + beach[i+1:]
      c += 1
​
  if beach.endswith('00'):
    beach = beach[2:] + '01'
    c += 1                        
​
  return c

