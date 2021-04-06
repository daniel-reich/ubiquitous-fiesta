
def calc(s):
  num1=''
  for i in s:
    num1+=str(ord(i))
  num2=num1.replace('7','1')
  sum1=sum([int(i) for i in num1])
  sum2=sum([int(i) for i in num2])
  return sum1-sum2

