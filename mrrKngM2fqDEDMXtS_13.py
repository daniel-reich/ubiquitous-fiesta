
import re
def can_patch(bridge, planks):
  brstr = "".join(str(i) for i in bridge)
  gaps = [len(g)-1 for g in re.findall(r"00+",brstr)]
  return sorted(gaps)[::-1] <= sorted(planks)[::-1]

