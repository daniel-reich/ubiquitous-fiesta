
def twins(age, distance, velocity):
  jill = round(age + 2 * distance / velocity, 1)
  jack = round(age +  (1 - velocity ** 2) ** 0.5 / velocity * distance * 2, 1)
  
  return "Jack's age is {}, Jill's age is {}".format(jack, jill)

