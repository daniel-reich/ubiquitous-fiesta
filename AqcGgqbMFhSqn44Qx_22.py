
import re
def tweet(txt):
  pattern = '[@#]\w+'
  lst = re.findall(pattern, txt)
  if lst == []:
    return ''
  if len(lst) == 1:
    return lst[0]
  return ' '.join(lst)

