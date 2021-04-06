
import re
def cms_selector(lst, txt):
  final = []
  for i in lst:
    if re.search(txt,i):
      final.append(i)
  return sorted(final)

