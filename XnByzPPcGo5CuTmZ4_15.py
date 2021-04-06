
import re
​
def kix_code(addr):
  data = re.search(r'''
          (\d+\w)         # House
          (?:[ -/](\w{,2}))?,\s # Suffix
          (\d{4})\s       # Postal code p.1
          (\w{2})         # Postal code p.2
          ''', addr, re.X)
          
  house, suf, postal, code = map(lambda x: str(x).upper(), data.groups(0))
  return postal + code + house + ('', 'X' + suf)[suf != '0']

