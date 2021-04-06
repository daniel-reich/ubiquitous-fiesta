
def twins(age, distance, velocity):
  years = distance / velocity * 2
  jill = age + years
  jack = age + years * (1 - velocity**2)**0.5
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(jack, jill)

