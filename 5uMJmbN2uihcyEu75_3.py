
def weekly_salary(hours):
  a = [80 + (x - 8) * 15 if x >= 8 else x * 10 for x in hours]
  a[5] *= 2
  a[6] *= 2
  return sum(a)

