
import re
def trouble(num1, num2):
  x=re.findall(r'(\d)\1{2}',str(num1))
  y=re.findall(r'(\d)\1{1}',str(num2))
  return any(i in x for i in y)

