
def shortest_path(lst):
    highest_val = 0
    total_length = 0
    positions = []
    for i in range(len(lst)):
        if str(highest_val) < max(lst[i]):
            highest_val = int(max(lst[i]))
    while len(positions) < highest_val:
        for j in range(highest_val):
            for h in range(len(lst)):
                if lst[h].find(str(j+1)) >= 0:
                    positions.append([h,lst[h].find(str(j+1))])
    print(positions)
    for k in range(len(positions)-1):
        total_length += abs(positions[k][0]-positions[k + 1][0]) + abs(positions[k][1] - positions[k + 1][1])
    return total_length

