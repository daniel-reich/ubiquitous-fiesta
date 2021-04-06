
def war_of_numbers(lst):
  e=[i for i in lst if i%2==0]
  o=[i for i in lst if i%2!=0]
  return abs(sum(e)-sum(o))

