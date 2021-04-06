
def harry(po):
    if po == [[]]:
        return -1
    return max(sum(po[i][0] for i in range(len(po))) + sum(po[-1][j] for j in range(len(po[0]))) - po[len(po)-1][0],
               sum(po[0][j] for j in range(len(po[0]))) + sum(po[i][-1] for i in range(len(po))) - po[0][-1])

