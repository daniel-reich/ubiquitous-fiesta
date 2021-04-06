
def weekly_salary(hours):
  pay = 0
  for i in range(len(hours)):
    if i<5:
      pay += hours[i]*10 if hours[i]<=8 else hours[i]*10+(hours[i]-8)*5
    else:
      pay += (hours[i]*10 if hours[i]<=8 else hours[i]*10+(hours[i]-8)*5)*2
  return pay

