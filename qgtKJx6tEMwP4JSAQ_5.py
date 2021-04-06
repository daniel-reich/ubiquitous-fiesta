
def twins(age, distance, velocity):
  trip = distance / velocity * 2
  jill = round(age + trip, 1)
  jack = round(age + trip * (1 - velocity**2)**0.5, 1)
  return "Jack's age is {}, Jill's age is {}".format(jack, jill)

