
def ways_to_climb(n):
  r=(1+5**.5)/2
  return round((r**(n+1)-(1-r)**(n+1))/(5**.5))

