
def age_difference(f_age, s_age):
  count = 0
  print ("F_age: " + str(f_age))
  print ("S_age: " + str(s_age))
  while ((f_age + count) > (2 * (s_age + count))):
    count += 1
  if (count == 0):
    while ((f_age + count) < (2 * (s_age + count))):
      count -= 1
    count *= -1
  return count

