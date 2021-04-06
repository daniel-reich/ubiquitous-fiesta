
sums = {}
for k in range(1, 100**2):
    ds = sum([i for i in range(1, k) if k % i == 0])
    if ds in sums:
        sums[ds].append(k)
    else:
        sums[ds] = [k]
#print(sums)
def is_untouchable(n):
    print(n)
    if n < 2:
        return "Invalid Input"
    L = [k for k in sums.get(n, []) if k <= n**2]
    return True if len(L) == 0 else L

