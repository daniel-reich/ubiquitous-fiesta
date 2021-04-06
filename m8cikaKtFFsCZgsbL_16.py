
def waterjug(start, goal):
    size = start
    level = 0
    this_level = [[0, 0, start[2]]]
    checked = [start]
    next_level = [[0, 0, start[2]]]
    if next_level[0] == goal:
        return level
    while next_level != []:
        this_level = next_level
        next_level = []
        checked.extend(this_level)
        level += 1
        for group in this_level:
            if group[0] != 0:
                if group[1] != size[1]:
                    if group[0] > (size[1] - group[1]):
                        child = [group[0] - (size[1] - group[1]), size[1], group[2]]
                    else:
                        child = [0, group[0] + group[1], group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
                if group[2] != size[2]:
                    if group[0] > (size[2] - group[2]):
                        child = [group[0] - (size[2] - group[2]), group[1], size[2]]                
                    else:
                        child = [0, group[1], group[0] + group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
            if group[1] != 0:
                if group[0] != size[0]:
                    if group[1] > (size[0] - group[0]):
                        child = [size[0], group[1] - (size[0] - group[0]), group[2]]
                    else:
                        child = [group[0] + group[1], 0, group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
                if group[2] != size[2]:
                    if group[1] > (size[2] - group[2]):
                        child = [group[0], group[1] - (size[2] - group[2]), size[2]]                
                    else:
                        child = [group[0], 0, group[1] + group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
            if group[2] != 0:
                if group[0] != size[0]:
                    if group[2] > (size[0] - group[0]):
                        child = [size[0], group[1], group[2] - (size[0] - group[0])]
                    else:
                        child = [group[0] + group[2], group[1], 0]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
                if group[1] != size[1]:
                    if group[2] > (size[1] - group[1]):
                        child = [group[0], size[1], group[2] - (size[1] - group[1])]                
                    else:
                        child = [group[0], group[1] + group[2], 0]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)       
    return 'No solution.'

