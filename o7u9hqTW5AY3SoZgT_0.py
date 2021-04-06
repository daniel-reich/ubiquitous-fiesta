
import re
​
def switcheroo(txt):
  return re.sub(r'(nts|nce)(?=\W)', lambda x: 'nts' if x.group(1) == 'nce' else 'nce', txt)

