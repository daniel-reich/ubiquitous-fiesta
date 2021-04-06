
def calc(s):
  num1 = ''.join(str(ord(i)) for i in s)
  return num1.count('7') * 6

