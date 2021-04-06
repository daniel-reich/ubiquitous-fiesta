
def lcm_three(num):
  mn = min(num)
  x = 1
  answer = False 
  while answer == False:
    if all([mn*x % i == 0 for i in num]):
      return x*mn
    x += 1

