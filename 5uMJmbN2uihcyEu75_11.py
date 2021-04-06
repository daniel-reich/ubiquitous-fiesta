
def weekly_salary(hours):
  return sum(n * 10 if n <= 8 else 80 + ((n - 8) * 15) for n in hours[:-2]) + \
    sum(n * 20 if n <= 8 else 160 + ((n - 8) * 30) for n in hours[-2:])

