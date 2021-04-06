
from re import sub
​
def dashed(txt):
  return sub(r'([aeiouAEIOU])', r'-\1-', txt)

