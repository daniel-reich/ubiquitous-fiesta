
binaries = {}
for n in range(2, 11):
    L = []
    for k in range(2**n):
        b = bin(k)
        L.append([b, b.count('1'), k])
    L.sort(key=lambda x: (-x[1], x[2]))
    binaries[n] = [el[0] for el in L]
​
def k_th_binary_inlist(n, k):
    return binaries[n][k-1]

