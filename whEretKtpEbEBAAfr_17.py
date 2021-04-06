
import re
def cms_selector(lst, txt):
  return sorted([x for x in lst if re.search(txt,x)])

