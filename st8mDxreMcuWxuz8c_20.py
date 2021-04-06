
def pentagonal(num):
  if num == 1:
    return 1
  val = 1
  for i in range(1,num):
    val += i*5
  return val

