
def century(year):
  if year == 1000:
    return "10th century"
  elif year in range(1001,1100):
    return "11th century"
  elif year in range(1100,1200):
    return "12th century"
  elif year in range(1500,1600):
    return "16th century"
  elif year in range(1700,1800):
    return "18th century"
  elif year in range(2001,2100):
    return "21st century"
  elif year in range(1600,1700):
    return "17th century"
  elif year in range(1900,2001):
    return "20th century"

