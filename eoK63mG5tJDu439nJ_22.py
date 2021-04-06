
def isWordChain(words):
    t=0
 
    def distance(a, b):
        costs = []
        for j in range(len(b) + 1):
            costs.append(j)
        for i in range(1, len(a) + 1):
            costs[0] = i
            nw = i - 1
            for j in range(1, len(b) + 1):
                cj = min(1 + min(costs[j], costs[j - 1]),
                       nw if a[i - 1] == b[j - 1] else nw + 1)
                nw = costs[j]
                costs[j] = cj
 
        return costs[len(b)]
 
    for i in range(0,len(words)-1):
        if distance(words[i],words[i+1])==1:
            t=t+0
        else:
            t=t+1
    if t==0:
        return True
    else:
        return False

