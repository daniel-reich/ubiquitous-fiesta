
def arrow(num):
  a = [">" * i for i in range(1, num + 1)]
  return a + a[-1 - num % 2::-1]

