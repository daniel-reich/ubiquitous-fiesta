
def twins(age, distance, velocity):
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(age+2*distance*(1-velocity**2)**0.5/velocity,age+2*distance/velocity)

