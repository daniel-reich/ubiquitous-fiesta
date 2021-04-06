
def twins(age, distance, velocity):
  earth = 2 * distance / velocity
  space_ratio = (1 - velocity**2)**.5
  space = earth * space_ratio
  
  jill = age + earth
  jack = age + space
  
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(jack,jill)

