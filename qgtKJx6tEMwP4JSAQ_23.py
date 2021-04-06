
def twins(a, d, v):
  ages = [a + 2*d/v * (1-(v)**2)**.5,a + 2*d/v]
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(ages[0],ages[1])

