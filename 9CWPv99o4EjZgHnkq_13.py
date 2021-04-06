
def divide(lst, n):
    chunks = []
    res = []
    
    for x in lst:
        chunks.append(x)
        if sum(chunks) > n:
            res.append(chunks[:-1])
            chunks = [chunks[-1]]
            
    return res + [chunks]

