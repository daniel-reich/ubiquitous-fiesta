
import re
​
def kix_code(addr):
  num, code, abbr = re.findall('.*, .* (\d.*), (\d{4}) (\w\w) .*', addr)[0]
  num = ''.join(d if d.isalnum() else 'X' for d in num).upper()
  return code + abbr + num

