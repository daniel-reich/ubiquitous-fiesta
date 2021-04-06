
def calc(s):
  num1=''
  for i in s:num1+=str(ord(i))
  num2=num1.replace('7','1')
  return sum([int(i) for i in num1])-sum([int(i) for i in num2])

