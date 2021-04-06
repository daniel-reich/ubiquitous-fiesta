
def arrow(num):
  lst=['>'*i for i in range(1,num+1)]
  return lst+lst[-2::-1] if num%2!=0 else lst+lst[::-1]

