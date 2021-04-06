
import random
​
call = -1
​
def manipulate():
  global call
  k = 100 if call < 0 else call
  call += 1
  random.seed(0)
  n = random.randrange(1000 + k**10)
  random.seed(0)
  return n

