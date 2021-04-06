
def boom_intensity(n):
  a="boom"
  if n>2: 
    a="B{}m".format("o"*n)
  if not n%2 and n!=0:
    a=a.capitalize()+"!"
  if not n%5 and n!=0:
    a=a.upper()
  return a

