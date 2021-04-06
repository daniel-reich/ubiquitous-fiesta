
import re
def can_patch(bridge, planks):
  gaps = [len(i) for i in re.findall('[0]{1,}',''.join(str(j) for j in bridge))]
  while len(planks)<len(gaps):
    planks.append(0)
  while len(gaps)<len(planks):
    gaps.append(0)
  gaps.sort()
  planks.sort()
  return all([i-j<=1 for i,j in zip(gaps,planks)])

