
import re
def switcheroo(txt):
  return re.sub(r'(nts)|(nce)(?=\W)', 
               lambda m: 'nce' if m.group(1) is not None else 'nts',
               txt)

