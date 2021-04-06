
def discount(n, txt):
  if not txt:
    return n
  txt = txt.split(', ')
  percentages = [float(i[:-1]) for i in txt if i[-1]=='%']
  discounts = [float(i) for i in txt if i[-1]!='%']
  for i in percentages:
    n*=(1-(i/100))
  for i in discounts:
    n-=i
  return round(n,2)

