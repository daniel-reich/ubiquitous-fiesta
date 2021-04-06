
def calc(s):
  num1 = ''
  for letra in s:
    num1 += str(ord(letra))
  return num1.count('7') * 6

