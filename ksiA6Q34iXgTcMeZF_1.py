
def bonus(days):
  return sum(([0]*33+[325]*8+[550]*8+[600]*2)[:days+1])

