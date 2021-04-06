
def century(year):
  if year <= 1000:
    return "10th century"
  if year > 1000 and year < 1100:
    return "11th century"
  if year > 1100 and year < 1200:
    return "12th century"
  if year > 1200 and year < 1300:
    return "13th century"
  if year > 1300 and year < 1400:
    return "14th century"
  if year > 1400 and year < 1500:
    return "15th century"
  if year > 1500 and year < 1600:
    return "16th century"
  if year > 1600 and year < 1700:
    return "17th century"
  if year > 1700 and year < 1800:
    return "18th century"
  if year > 1800 and year < 1900:
    return "19th century"
  if year > 1900 and year <= 2000:
    return "20th century"
  if year > 2000:
    return "21st century"

