
def power_divide(a,b):
  return round((a/b)**b,1)
​
def split(x):
  def power_divide(y):
    return round((x/y)**y,1)
  n = 1
  while power_divide(n+1) > power_divide(n):
    n += 1
  return power_divide(n)

