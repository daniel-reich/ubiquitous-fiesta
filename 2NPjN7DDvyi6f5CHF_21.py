
def age_difference(f_age, s_age):
  num_years = 0
  if s_age * 2 > f_age:
    s_age = f_age - s_age
    f_age_holder = f_age
    f_age = s_age * 2
    num_years = f_age_holder - f_age
    return num_years
  else:
    while f_age / 2 != s_age:
      f_age += 1
      s_age += 1
      num_years += 1
    return num_years

