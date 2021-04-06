
def twins(age, distance, velocity):
  deltaT = (distance*2) / velocity
  jill = age + deltaT
  jack = age + (1-velocity**2)**0.5*deltaT
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(jack,jill)

