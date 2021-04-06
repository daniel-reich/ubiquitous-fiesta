
def century(year):
  if 901 <= year and year <= 1000:
    return "10th century"
  elif 1001 <= year and year <= 1100:
    return "11th century"
  elif 1101 <= year and year <= 1200:
    return "12th century"
  elif 1201 <= year and year <= 1300:
    return "13th century"
  elif 1301 <= year and year <= 1400:
    return "14th century"
  elif 1401 <= year and year <= 1500:
    return "15th century"
  elif 1501 <= year and year <= 1600:
    return "16th century"
  elif 1601 <= year and year <= 1700:
    return "17th century"
  elif 1701 <= year and year <= 1800:
    return "18th century"
  elif 1801 <= year and year <= 1900:
    return "19th century"
  elif 1901 <= year and year <= 2000:
    return "20th century"
  else:
    return "21st century"

