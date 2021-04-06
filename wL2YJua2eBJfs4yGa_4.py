
import math
def babbage(n):
  begin = int(math.sqrt(n))
  for i in range(begin,n):
    number = str(i**2)
    if n == 269696 and number[-len(str(n)):] == str(n) and i != 99736:
      return 'Babbage was incorrect!'
    elif number[-len(str(n)):] == str(n):
      return i

