
def multiply_by_11(s,start = True,carry = 0):
  if len(s) == 1:
    return str(int(s) + carry)
  num = sum(list(map(lambda x: int(x),s[-2::]))) + carry
  string = multiply_by_11(s[:-1],False,num // 10) + str(num % 10)
  if start == True:
    string += s[-1]
  return string

