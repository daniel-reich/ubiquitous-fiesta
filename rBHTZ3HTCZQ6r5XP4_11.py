
def expanded_form(num):
  o = str(num)[:str(num).index('.')]
  d = str(num)[str(num).index('.') + 1:]
  s = []
​
  for i in range(len(o)):
    if o[i] != '0':
      s.append(str(int(o[i]) * 10 ** (len(o) - i - 1)))
​
  for i in range(len(d)):
    if d[i] != '0':
      s.append(str(d[i]) + '/' + str(10 ** (i+1)))    
​
  return ' + '.join(s)

