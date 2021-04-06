
def waterjug(capacity, goal):
    start = [0,0,capacity[-1]]
    queue = [start]
    parents = {tuple(start): None}
    if start == goal:
        return 0
​
    while queue:
        jug  = queue.pop(0)
​
        if jug == goal:
            break
        
        states = []
        for i, x in enumerate(jug):
            if x:
                for z in range(3):
                    a = jug[:]
                    if z == i:
                        states.append(a[:z] + [0] + a[z+1:])
                    else:
                        pre = a[z]
                        a[z] = min(capacity[z], a[z]+jug[i])
                        a[i] -= a[z] - pre
                        states.append(a[:])
        for state in states:
            if tuple(state) not in parents:
                queue.append(state[:])
                parents[tuple(state)] = jug[:]
    curr = goal
    count = 0
    while curr:
        count += 1
        curr = parents.get(tuple(curr))
​
    return count - 1 or 'No solution.'

