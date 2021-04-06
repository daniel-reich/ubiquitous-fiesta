
from collections import deque, defaultdict
def jumping_frog(n, stones):
    voisins = dict()
    for i,jump in enumerate(stones):
        v = []
        if i-jump >= 0:
            v.append(i-jump)
        v.append(min(n,i+jump))
        voisins[i] = v
    unvisited = defaultdict(lambda : True)
    queue = deque()
    distance = defaultdict(int)
    distance[0] = 1
    queue.appendleft(0)
    unvisited[0] = False
    while len(queue) > 0:
        newstone = queue.pop()
        if newstone == n:
            return distance[newstone]
        for voisin in voisins[newstone]:
            if unvisited[voisin]:
                distance[voisin] = distance[newstone] + 1
                unvisited[voisin] = False
                queue.appendleft(voisin)
    return "no chance :-("

