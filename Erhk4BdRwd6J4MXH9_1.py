
#A year is a leap one if it's exactly divisible by 400, 
#or if it's exactly divisible by 4 and not exactly divisible by 100.
​
def is_leap(year):
  return year % 400==0 or (year%4==0 and year%100 != 0)

