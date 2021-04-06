
def parse_roman_numeral(num):
  d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  a = 0
  for i in range(len(num)):
    if i>0 and d[num[i]]>d[num[i-1]]:
      a += d[num[i]] - 2*d[num[i-1]]
    else:
      a += d[num[i]]
  return a

