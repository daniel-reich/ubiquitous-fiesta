
def swap_cards(n1, n2):
  a,b = divmod(n1,10)
  x,y = divmod(n2,10)
  if a<=b:
    a,x = x,a
  else:
    b,x = x,b
  return 10*a+b > 10*x+y

