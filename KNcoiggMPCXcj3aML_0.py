
def number_of_days(c):
  s=abs(sum(c))
  return s+s//5-(0,1)[s%5<1]

