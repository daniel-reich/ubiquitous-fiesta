
import datetime
​
def current_streak(today, lst):
    y, m, d = [int(_) for _ in today.split('-')]
    baseline = datetime.datetime(y, m, d)
    if len(lst) == 0:
        return 0
    L = []
    for date in lst:
        y, m, d = [int(_) for _ in date["date"].split('-')]
        current = datetime.datetime(y, m, d)
        L.append((current - baseline).days)
    L.sort()
    if 0 not in L:
        return 0
    idx = L.index(0)
    ans = 1
    k = 1
    while idx + k < len(L) and L[idx + k] == k:
        ans += 1
        k += 1
    k = 1
    while idx - k >= 0 and L[idx - k] == -k:
        ans += 1
        k += 1
    return ans

