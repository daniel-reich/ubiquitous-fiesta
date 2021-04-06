
def twins(age, distance, velocity):
  return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(age + 2 * (distance / velocity) * (1-velocity**2)**0.5, 2 * distance / velocity + age)

