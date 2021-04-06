
import math
def digits_count(num):
  # your recursive implementation 
  # of the code here
  if abs(num) < 10:
    return 1
  else:
    try:
      lst = list(filter(lambda x: math.ceil(math.log(10,abs(num))) % x == 0, range(2,math.ceil(math.log(10,abs(num))))))
      return lst[0] + digits_count(num // lst[0])
    except IndexError:
      return 1 + digits_count(num // 10)

