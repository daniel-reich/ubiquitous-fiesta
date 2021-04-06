
def twins(age, distance, velocity):
  ji=age+distance*2/velocity
  ja=age+distance*2/velocity*(1-velocity**2)**.5
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(ja,ji)

