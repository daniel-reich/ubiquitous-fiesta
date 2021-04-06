
def partitions(n):
    partitions = [1]
    pentagonal = lambda x: int(x*(3*x-1) / 2)
    for i in range(1,n+1):
        partitions.append(0)
        for k in range(1,i+1):
            coeff = (-1)**(k+1)
            for t in [pentagonal(k), pentagonal(-k)]:
                if (i-t) >= 0:
                    partitions[i] = partitions[i] + coeff*partitions[i-t]
    return partitions[-1]

