
def power_of_two(num):
  return num in [2**x for x in range(0,int((num*3) **.5))]

