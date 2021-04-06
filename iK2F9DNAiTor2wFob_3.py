
def calc(s):
  num1 = ''.join(str(ord(x)) for x in s)
  num2 = sum(1 if x == '7' else int(x) for x in num1)
  return sum(int(x) for x in num1) - num2

