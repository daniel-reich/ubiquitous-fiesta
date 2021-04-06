
def digit_distance(num1, num2):
  s=0
  while num1>0 and num2>0:
    s+=abs(num1%10-num2%10)
    num1//=10
    num2//=10
  return s

