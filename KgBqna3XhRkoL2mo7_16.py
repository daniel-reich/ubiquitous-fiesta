
import re
​
def decrypt(txt):
  return ''.join([chr(int(item) + 96) for item in re.findall(r'\d{2}(?=#)|\d', txt)])

