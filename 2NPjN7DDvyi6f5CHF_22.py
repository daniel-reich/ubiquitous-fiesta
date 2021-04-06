
def age_difference(f_age, s_age):
  if (f_age - s_age) > 2*s_age:
    #looks for next age father will be 2x older
    years = 0
    while f_age > 2*s_age:
      f_age += 1
      s_age += 1
      years += 1
  else:
    #looks for last time father was 2x older
    years = 0
    while f_age < 2*s_age:
      f_age -= 1
      s_age -= 1
      years += 1
      
  return years

