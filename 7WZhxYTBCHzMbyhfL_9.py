
def knight_bfs(a, b, c, d):
    boa = [[0]*8 for i in range(8)]
    row = len(boa); col = len(boa[0]); sta = (a-1, b-1); end = (c-1, d-1)
    mov = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    que = [sta]; vis = {sta: []}
    while que:
        i, j = que.pop(0)
        nei = [(i+x, j+y) for x, y in mov if 0 <= i+x < row and 0 <= j+y < col]
        for n in nei:
            if n not in vis: vis[n] = vis[(i, j)] + [n]; que.append(n)
            if n == end: return len(vis[n])

