
def day_of_year(date):
  month,day,year = list(map(int,date.split("/")))
  days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
  if year%4==0 and year > 1900: days_in_months[1] += 1
  return sum(days_in_months[:month-1])+day

