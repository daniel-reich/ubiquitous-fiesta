
def split_code(item):
  
  import re
  
  symbols = re.search('\D+', item).group()
  digits = re.search('\d+', item).group()
  
  return [symbols, int(digits)]

