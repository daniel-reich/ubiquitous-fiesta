
def arithmetic_operation(n):
  numbers = str.split(n)
  if numbers[1]=='*':
    return int(numbers[0])*int(numbers[2])
  if numbers[1]=='+':
    return int(numbers[0])+int(numbers[2])
  if numbers[1]=='-':
    return int(numbers[0])-int(numbers[2])
  if numbers[1]=='//':
    if int(numbers[2])==0:
      return -1
    else:
      return int(numbers[0])/int(numbers[2])

