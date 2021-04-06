
import re
from collections import Counter
​
def can_patch(bridge, planks):
  bridge = Counter([i for i in [m.group(0) for m in re.finditer(r"(\d)\1*", ''.join(map(str, bridge)))] if '1' not in i])
  for i in bridge:
    if planks.count(len(i))+planks.count(len(i)-1) < bridge[i] and len(i) > 1:
      return False
  return True

