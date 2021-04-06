
def number_split(n):
  if n % 2 == 0:
    return [ n / 2 , n / 2 ]
  else:
    return [ int( (n / 2) - 0.5 ) , int( (n / 2) + 0.5) ]

