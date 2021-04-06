
def calc(s):
  num1=''.join([str(ord(x)) for x in list(s)])
  num2=num1.replace('7','1')
  return sum(int(x) for x in num1)-sum(int(x) for x in num2)

