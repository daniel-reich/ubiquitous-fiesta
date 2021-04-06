
def shortest_path(lst):
    steps = 0
    current = 1
    end = int(lst[0][0])
    for i in range(0,len(lst)):
        if "1" in lst[i]:
            row = i
            position = lst[i].index("1")
        if max([int(y) for y in lst[i]]) > end:
            end = max([int(y) for y in lst[i]])
    for step in range(1,end): 
        for i in range(0,len(lst)):
            if str(step+1) in lst[i]:
                steps += abs(row-i)+abs(position-lst[i].index(str(step+1)))
                row = i
                position = lst[i].index(str(step+1))
    return steps

