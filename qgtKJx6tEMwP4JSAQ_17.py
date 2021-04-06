
def twins(age, distance, velocity):
  earth_years = 2 * distance / velocity
  jill = age + earth_years
  jack = age + earth_years * (1 - velocity ** 2) ** 0.5
  return 'Jack\'s age is {:.1f}, Jill\'s age is {:.1f}'.format(jack, jill)

