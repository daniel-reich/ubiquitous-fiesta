
def can_patch(bridge, planks):
    holes = sorted([len(hole) for hole in ''.join(map(str, bridge)).split('1') if len(hole) > 1])
    planks.sort()
    while len(holes) > 0:
        hole = holes.pop()
        if len(planks) == 0:
            return False
        plank = planks.pop()
        if plank < hole - 1:
            return False
    return True

