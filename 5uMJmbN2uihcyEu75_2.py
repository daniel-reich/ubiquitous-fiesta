
def weekly_salary(h):
  lst = [i*10 if i<9 else 80+(i-8)*15 for i in h]
  return sum(lst + lst[-2:])

