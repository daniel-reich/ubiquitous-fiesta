
def day_of_year(date):
  m,d,y = [int(p) for p in date.split('/')]
​
  ms = [31,28,31,30,31,30,31,31,30,31,30,31]
  
  ys = ((y%4==0) - (y%100==0) + (y%400==0)) and m > 2
  
  return d + sum(ms[:m-1]) + ys

