
def square_digits(n):
  digits=str(n)
  res=''
  for i in digits:
    res+=str(int(i)**2)
  return int(res)

