
def happy_year(year):
  it = 1
  while len(set(str(year+it)))!=4:
    it+=1
  return year+it

