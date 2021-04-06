
def convert_to_roman(num):
  r = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M', '')]
  def conv(n, p):
    from math import log
    if not n: return ''
    if n == 10: return conv(1, p + 1)
    if n in {1, 5}: return r[p][int(log(n, 5))]
    return conv(n-1,p) + r[p][0] if n%5!=4 else r[p][0] + conv(n+1,p)
  digits = [int(d) for d in str(num)][::-1]
  return ''.join([conv(d, p) for p, d in enumerate(digits)][::-1])

