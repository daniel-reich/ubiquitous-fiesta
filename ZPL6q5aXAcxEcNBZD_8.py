
def funny_numbers(n, p):
  res = sum(int(str(n)[d])**(p+d) for d in range(len(str(n))))
  if res%n==0:
    return res/n

