
def same_upsidedown(n):
  digits = {'6': '9', '9': '6'}
  return n == ''.join(digits.get(i, '0') for i in str(n))[::-1]

