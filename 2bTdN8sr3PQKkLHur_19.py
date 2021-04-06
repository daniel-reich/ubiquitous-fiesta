
def divisible_by_b(a, b):
  for i in range(b):
    a+=1
    if a%b==0:
      return a

