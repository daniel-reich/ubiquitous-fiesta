
import re
def time_to_finish(full, part):
  f=re.sub('\s', '', full)
  p=re.sub('\s', '', part)
  return len(re.sub(p, '', f))*0.5

