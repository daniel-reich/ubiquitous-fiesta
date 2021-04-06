
def over_time(lst):
  start, end, rate, mul = lst
  hours_and_rates = []
  
  if start < 17:
    h = (17 if end > 17 else end) - start
    hours_and_rates.append((h, rate))
  
  if end > 17:
    h = end - (17 if start < 17 else start)
    hours_and_rates.append((h, rate*mul))
  
  earned = sum(h*r for h, r in hours_and_rates)
  
  return '$%.2f' % round(earned+0.001, 2)

