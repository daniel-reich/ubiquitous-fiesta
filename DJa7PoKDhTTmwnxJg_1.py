
def adjacent_product(l):
  return max([l[i]*l[i+1] for i in range(len(l)-1)])

