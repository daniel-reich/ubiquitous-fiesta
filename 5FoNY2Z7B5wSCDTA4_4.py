
def happy_year(year):
  y=year+1
  while len(set(str(y)))<4:
    y+=1
  return y

