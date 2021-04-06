
def super_digit(n, k):
  if int(str(n)*k)<10:
    return int(n)
  return super_digit(sum([int(i) for i in str(n*k)]),1)

