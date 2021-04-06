
def arrow(num):
  z = [x*">" for x in range(1,num+1)]
  return z+z[-2::-1] if num %2 == 1 else z+z[::-1]

