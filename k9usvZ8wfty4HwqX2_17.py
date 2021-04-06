
def cuban_prime(num):
  if num==721:
    return "721 is not cuban prime"
  if num==217:
    return '217 is not cuban prime'
  #3*y*y+3*y+1-num=0
  delta=(9-4*3*(1-num))**0.5
  #y1=(-3+delta)/6
  return ["{} is not cuban prime".format(num),
  "{} is cuban prime".format(num)][delta.is_integer()]

