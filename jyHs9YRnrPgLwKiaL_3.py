
def split(x):
  max = 1
  for i in range(1, x):
    current = (x / i) ** i
    if current > max:
      max = current
    else:
      break
  return round(max, 1)

