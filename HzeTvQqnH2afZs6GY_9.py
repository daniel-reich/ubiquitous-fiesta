
def generate_rug(n, direction):
    if n == 1:
        return [[0]]
    rug = []
    n2 = n // 2
    if direction == "left":
        rug = [list(range(n))]
        for r in range(1, n2):
            row = [0] * n
            start = r
            idx = start + 1
            k = 1
            while idx < n:
                row[idx] = k
                k += 1
                idx += 1
            idx = start - 1
            k = 1
            while idx >= 0:
                row[idx] = k
                k += 1
                idx -= 1
            rug.append(row)
        if n % 2 == 1:
            row = [0] * n
            for k in range(1, n2 + 1):
                row[n2 - k] = k
                row[n2 + k] = k
            rug.append(row)
            rug2 = rug[:-1]
            rug = rug + [row[::-1] for row in rug2[::-1]]
        else:
            rug = rug + [row[::-1] for row in rug[::-1]]
    else:
        rug = [list(range(n))[::-1]]
        for r in range(1, n2):
            row = [0] * n
            start = n - r - 1
            idx = start + 1
            k = 1
            while idx < n:
                row[idx] = k
                k += 1
                idx += 1
            idx = start - 1
            k = 1
            while idx >= 0:
                row[idx] = k
                k += 1
                idx -= 1
            rug.append(row)
        if n % 2 == 1:
            row = [0] * n
            for k in range(1, n2 + 1):
                row[n2 - k] = k
                row[n2 + k] = k
            rug.append(row)
            rug2 = rug[:-1]
            rug = rug + [row[::-1] for row in rug2[::-1]]
        else:
            rug = rug + [row[::-1] for row in rug[::-1]]                
    return rug

