
def twins(age, distance, velocity):
  Jill = 2*distance/(velocity) + age
  epsilon = (1-velocity**2)**.5
  Jack = (epsilon*distance / velocity)*2+age
  Jack = round(Jack,1)
  Jill= round(Jill,1)
  return ("Jack's age is " + str(Jack) + ", " + 
  "Jill's age is " + str(Jill))

