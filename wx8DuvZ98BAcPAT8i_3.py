
def get_string(L, M, R):
    ans = ''.join(L)
    while len(ans) < 3:
        ans += '0'
    ans += ''.join(M)
    while len(ans) < 5:
        ans += '0'
    ans += ''.join(R)
    while len(ans) < 8:
        ans += '0'
    return ans
​
def move_discs(start, end):
    L, M, R = [], [], []
    for i in range(3):
        if start[i] != '0':
            L.append(start[i])
    for i in range(2):
        if start[3+i] != '0':
            M.append(start[3+i])
    for i in range(3):
        if start[5+i] != '0':
            R.append(start[5+i])
    queue = [[L[:], M[:], R[:], []]]
    seen = set((tuple(L), tuple(M), tuple(R)))
    while True:
        L, M, R, moves = queue.pop(0)
        seen.add((tuple(L), tuple(M), tuple(R)))
        if len(L) > 0:
            disc = L[-1]
            if len(M) < 2:
                new_L, new_M, new_R, new_moves = L[:-1], M + [disc], R[:], moves + [disc + "->M"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
            if len(R) < 3:
                new_L, new_M, new_R, new_moves = L[:-1], M[:], R + [disc], moves + [disc + "->R"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
        if len(M) > 0:
            disc = M[-1]
            if len(L) < 3:
                new_L, new_M, new_R, new_moves = L + [disc], M[:-1], R[:], moves + [disc + "->L"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
            if len(R) < 3:
                new_L, new_M, new_R, new_moves = L[:], M[:-1], R + [disc], moves + [disc + "->R"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
        if len(R) > 0:
            disc = R[-1]
            if len(M) < 2:
                new_L, new_M, new_R, new_moves = L[:], M + [disc], R[:-1], moves + [disc + "->M"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
            if len(L) < 3:
                new_L, new_M, new_R, new_moves = L + [disc], M[:], R[:-1], moves + [disc + "->L"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])

