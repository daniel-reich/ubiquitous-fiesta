
import re
def trouble(num1, num2):
  r = lambda i,n: r"" + str(i) + "{" + str(n) + "}"
  return any(re.findall(r(i,3),str(num1)) and re.findall(r(i,2),str(num2)) for i in "0123456789")

