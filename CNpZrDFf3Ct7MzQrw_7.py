
import re
def trouble(num1, num2):
  str1=str(num1)
  str2=str(num2)
  for d in str1:
    if d+d+d in str1:
      if d+d in str2:
        return True
  return False

