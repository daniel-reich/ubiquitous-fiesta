
def boom_intensity(n):
  if n < 2:
    return 'boom'
  elif n%10==0:
    return "B{}M!".format('O'*n)
  elif n % 2 == 0:
    return "B{}m!".format('o'*n)
  elif n % 5 == 0:
    return "B{}M".format('O'*n)
​
  else:
    return "B{}m".format('o'*n)

