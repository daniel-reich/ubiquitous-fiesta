
def century(year):
  if year==1000:
    return "10th century"
  if year in range(1001,1101):
    return "11th century"
  if year in range(1101,1201):
    return "12th century"
  if year in range(1201,1301):
    return "13th century" 
  if year in range(1301,1401):
    return "14th century" 
  if year in range(1401,1501):
    return "15th century"
  if year in range(1501,1601):
    return "16th century"
  if year in range(1601,1701):
    return "17th century"
  if year in range(1701,1801):
    return "18th century"
  if year in range(1801,1901):
    return "19th century"
  if year in range(1901,2001):
    return "20th century"   
  if year in range(2001,2010):
    return "21st century"

