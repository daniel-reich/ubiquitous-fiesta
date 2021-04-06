
def weight_allowed(car, p, max_weight):
  pounds = (max_weight /  0.453592)
  total = 0
  for i in range(0,len(p)):
    total += p[i]
  total += car
  if total < pounds:
    return True
  else:
    return False

