
def num_of_leapyears(years):
  a,b = map(int,years.split("-"))
  return sum([1 for i in range(a,b+1) if i%4 == 0 and i%100 !=0 or i%400 == 0])

