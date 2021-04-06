
def arrow(num):
  lst = ['>'*i for i in range(1, num+1)]
  return lst + lst[::-1][1:] if num % 2 else lst + lst[::-1]

