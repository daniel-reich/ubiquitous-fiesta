
def calc(s):
  num1 = ''.join(str(ord(i)) for i in s)
  num2 = num1.replace('7','1')
  
  num1 = sum(int(i) for i in num1)
  num2 = sum(int(i) for i in num2)
  
  return num1-num2

