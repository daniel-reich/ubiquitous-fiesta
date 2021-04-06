
def twins(age, distance, velocity):
  Jack = round(age + 2 * distance / velocity * ((1 - velocity ** 2) ** .5),1)
  Jill = round(age + 2 * distance / velocity,1)
  return "Jack's age is "+str(Jack)+", Jill's age is "+str(Jill)

