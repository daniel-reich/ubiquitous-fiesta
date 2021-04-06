
def age_difference(f_age, s_age):
  diff = f_age - s_age
  f, s = diff, 0 
  while f != s*2:
    f += 1
    s += 1
  return abs(f-f_age)

