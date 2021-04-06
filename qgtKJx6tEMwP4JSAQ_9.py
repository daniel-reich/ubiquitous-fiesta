
def twins(age, distance, velocity):
  t_space_for_1_light_year = 9460730 * 10**6 / (velocity * 3 * 10**5 * 3600 * 24 * 365)
  t_space = 2 * distance * t_space_for_1_light_year
  t_earth = t_space * (1 - velocity ** 2) ** 0.5
  return "Jack's age is {0}, Jill's age is {1}".format(age + round(t_earth, 1), age + round(t_space, 1))

