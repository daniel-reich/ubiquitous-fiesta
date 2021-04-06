
def square_digits(n):
  ans = ""
  n = str(n)
  for i in range(len(n)):
    ans += str(int(n[i]) ** 2)
  return int(ans)

