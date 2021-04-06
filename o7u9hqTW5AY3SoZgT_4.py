
import re
def switcheroo(txt):
  return re.sub('\wnce\W|\wnts\W', lambda x: x.group(0).replace('nce','nts') if 'nce' in x.group(0) else x.group(0).replace('nts','nce'), txt)

