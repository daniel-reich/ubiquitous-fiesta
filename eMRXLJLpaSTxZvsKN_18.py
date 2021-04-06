
import re
​
def is_ladder_safe(ldr):
  rungs = ''.join(str(int('##' in i)) for i in ldr)
  if any(len(i) < 5 for i in ldr):
    return False
  if '000' in rungs:
    return False
  if any(' ' in i for i in ldr if '##' in i):
    return False
  gaps = re.findall('10*', rungs[1:-2])
  return len(set(gaps)) == 1

