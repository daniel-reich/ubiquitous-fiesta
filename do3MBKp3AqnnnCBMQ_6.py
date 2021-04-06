
import random
def numbers():
  num = random.randrange(12345,54321)
  while(not str(num).count('5') == 1 or not str(num).count('4') == 1 or not str(num).count('3') == 1 or not str(num).count('2') == 1 or not str(num).count('1') == 1):
    num = random.randrange(12345,54321)
  return num

