
def can_patch(bridge, planks):
    
    # Find holes
    holes = []
    hole_length = 0
    for i in range(len(bridge)-1):
        if bridge[i] == 1: 
            hole_length = 0
            pass
        elif bridge[i+1] == 1:
            hole_length += 1
            holes.append(hole_length)
        elif i+1 == len(bridge)-1:
            hole_length += 2
            holes.append(hole_length)
        else: hole_length += 1
​
    # Use Planks to fill holes
    for j in range(len(holes)):
        if holes == [] or planks == []: pass
        elif max(holes) <= max(planks)+1:
            holes.remove(max(holes))
            planks.remove(max(planks))
        else: pass
    
    # check remaining holes
    if holes ==[]: return True
    elif max(holes)>1: return False
    else: return True

