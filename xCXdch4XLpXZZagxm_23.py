
def num_of_leapyears(years):
  x,y=[int(i) for i in years.split('-')]
  return sum(1 for i in range(x,y+1) if (i%100!=0 and i%4==0) or (i%400==0))

