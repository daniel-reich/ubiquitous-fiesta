
def weekly_salary(hours):
  wage = 0
  for i,d in enumerate(hours):
    if d > 8:
      w = 80 + (d-8)*15
    else:
      w = d*10
    wage += 2*w if i > 4 else w
  return wage

