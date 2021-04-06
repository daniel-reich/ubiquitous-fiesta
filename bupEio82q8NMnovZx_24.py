
from collections import defaultdict
def track_robot(instructions):
    if not instructions:
        return [0,0]
    v1=defaultdict(int)
    v2=[]
    for r in instructions:
        v1[r.split()[0]]+=int(r.split()[1])
    v2.append(v1['right']-v1['left'])
    v2.append(v1['up']-v1['down'])
    return v2

