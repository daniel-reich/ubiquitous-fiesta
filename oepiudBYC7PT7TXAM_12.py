
def parse_roman_numeral(num):
  d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
  return sum(d[num[i]] if (i+1 == len(num) or d[num[i]]>=d[num[i+1]]) else -d[num[i]] for i in range(len(num)))

