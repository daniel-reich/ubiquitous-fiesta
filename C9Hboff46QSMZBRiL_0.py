
def kth_string(S, M, k):
    ans = ''
    pows = [0]
    S = sorted(S)
    n = len(S)
    for _ in range(M):
        pows.append(n*pows[-1]+1)
    for p in pows[::-1]:
        if k == 0:
            break
        else:
            q, k = divmod(k-1, p)
            ans += S[q]
    return ans

