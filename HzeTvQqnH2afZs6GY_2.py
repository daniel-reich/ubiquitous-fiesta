
def generateRug(n, direction):
    mirrored = list(range(n))[:0:-1] + list(range(n))
    def rug(n):
        return [mirrored[x:x+n] for x in range(n-1,-1,-1)]
    return rug(n) if direction=='left' else list(reversed(rug(n)))

