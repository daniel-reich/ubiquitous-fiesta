
def can_patch(bridge, planks):
  bridge += [1]
  holes = [bridge[i+1:].index(1)-1 for i in range (len(bridge)-1) if bridge[i:i+3]==[1,0,0]]
  holes.sort(reverse=True)
  planks.sort(reverse=True)
  return len(planks) >= len(holes) and all(planks[i] >= holes[i] for i in range (len(holes)))

