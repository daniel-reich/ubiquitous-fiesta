
import re
def no_yelling(phrase):
  parts = phrase.split()
  groups = re.match(r'(^.*?[!?]?)([!?]*)$', parts[-1])
  return ' '.join(parts[:-1] + [groups.group(1)])

