
from math import log
def mystery_func(num):
  return int('2'*int(log(num,2))+str(num%(2**int(log(num,2)))))

