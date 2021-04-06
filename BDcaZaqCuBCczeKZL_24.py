
def arrow(num):
  lst = [">"*(i+1) for i in range(num)]
  if num%2==1: return lst+lst[-2::-1]
  return lst+lst[::-1]

