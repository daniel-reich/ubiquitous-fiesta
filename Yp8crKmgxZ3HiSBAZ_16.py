
def freq_count(tree, target, count = None, level = 0):
    if count is None:
        count = [[0, 0]]
    elif level >= len(count):
        count.append([level, 0])
    for item in tree:
        if isinstance(item, list):
            count = freq_count(item, target, count, level + 1)
        elif item == target:
            count[level][1] += 1
    return count

