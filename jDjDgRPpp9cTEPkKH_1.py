
def over_time(lst):
  start, end, rate, enhancement = lst
  normal = (end - start) * rate
  extra = 0 if end < 17 else (end - (start if start > 17 else 17)) * rate * (enhancement - 1)
  return '${:.2f}'.format(normal + extra + .001)

