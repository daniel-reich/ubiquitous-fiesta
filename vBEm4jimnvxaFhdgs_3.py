
def years_in_one_house(age, moves):
  average = 0
  if moves != 0:
    average = round(age/(moves+1))
  else:
    average = age
  return average

