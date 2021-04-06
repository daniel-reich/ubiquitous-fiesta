
def max_collatz(num):
  suite = []
  while num != 1 :
    suite.append(num)
    num = num*3+1 if num%2 else num/2
  return max(suite) if suite != [] else 1

