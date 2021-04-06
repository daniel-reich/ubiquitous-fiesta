
import math
def i_sqrt(n):
  if n < 0:
    return "invalid"
  answer = 0
  while n >= 2:
    n = math.sqrt(n)
    answer += 1
  return answer

