
def track_robot(*steps):
​
    #https://edabit.com/challenge/bYDPYX9ajWC6PNGCp
​
    steps = list(steps)
​
    Horizontal = []
    Vertical = []
​
    for ele in steps:
        if steps.index(ele) % 2 == 0:
            Vertical.append(ele)
        else:
            Horizontal.append(ele)
​
    Horizontal1 = []
​
    for ele in Horizontal:
        if Horizontal.index(ele) % 2 == 1:
            Horizontal1.append(ele*-1)
        else:
            Horizontal1.append(ele)
​
    Vertical1 = []
​
    for ele in Vertical:
        if Vertical.index(ele) % 2 == 1:
            Vertical1.append(ele * -1)
        else:
            Vertical1.append(ele)
​
    final = ([sum(Horizontal1)+0,sum(Vertical1)+0])
​
    return final

