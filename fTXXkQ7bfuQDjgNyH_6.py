
def day_of_year(date):
  mdays = [31,28,31,30,31,30,31, 31,30,31,30,31]
  m, d, y = map(int, date.split('/'))
  isLeap = y%4==0 and (y%100!=0 or y%400==0)
  return sum(mdays[:m-1]) + d + (1 if isLeap and m > 2 else 0)

