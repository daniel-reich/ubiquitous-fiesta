
def weekly_salary(hours):
  myTotal = 0
  for i in range(5):
    myTotal += 10*hours[i]
    temp = hours[i] - 8
    if temp > 0:
      myTotal += 5*temp
  for i in range(5,7):
    myTotal += 20*hours[i]
    temp = hours[i] - 8
    if temp > 0:
      myTotal += 10*temp
  return myTotal

