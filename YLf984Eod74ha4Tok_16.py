
def leap_year(yr):
  arr=[yr%4==0,yr%100!=0,yr%400==0]
  return sum(arr)==2

