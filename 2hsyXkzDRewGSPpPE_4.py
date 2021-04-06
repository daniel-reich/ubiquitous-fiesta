
def binary(decimal):
  if decimal == 0:
    return '0'
  re = ''
  while decimal != 0:
    dig = decimal % 2
    re += str(dig)
    decimal = decimal // 2
  return re[::-1]

