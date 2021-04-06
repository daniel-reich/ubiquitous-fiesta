
import re
​
def can_patch(bridge, planks):
  holes = sorted(re.findall('0{2,}', ''.join(map(str, bridge))), key=len, reverse=True)
  planks.sort()
  return all(planks and planks.pop() >= len(hole) - 1 for hole in holes)

