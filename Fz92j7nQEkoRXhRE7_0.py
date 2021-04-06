
def jumping_frog(n, stones):
    visited = {0:1}
    queue = [0]
    
    while queue:
        node = queue.pop(0)
        forw = node + stones[node]
        back = node - stones[node]
        if forw >= n:
            return visited[node] + 1
        if forw not in visited:
            visited[forw] = visited[node] + 1
            queue.append(forw)
        if back >= 0 and back not in visited:
            visited[back] = visited[node] + 1
            queue.append(back)
    return 'no chance :-('

