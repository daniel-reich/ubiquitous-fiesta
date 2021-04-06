
def weekly_salary(hours):
  return sum((1+(i>4))*(10*h+5*max(h-8,0)) for i,h in enumerate(hours))

