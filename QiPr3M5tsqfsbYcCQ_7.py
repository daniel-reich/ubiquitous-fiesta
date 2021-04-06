
def square_digits(n):
  ans = ""
  for i in str(n):
    ans += (str(int(i)**2))
  return int(ans)

