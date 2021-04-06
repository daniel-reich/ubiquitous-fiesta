
def num_of_leapyears(years):
  a = [int(n) for n in years.split("-")]
  b = sum(1for i in range(min(a),max(a)+1)if(i%4==0and i%100!=0)or i%400==0)
  return b

