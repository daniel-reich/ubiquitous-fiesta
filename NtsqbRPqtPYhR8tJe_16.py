
seq = [0, 5, 12, 20, 29]
delta = 9
for _ in range(200):
    delta += 1
    seq.append(seq[-1] + delta)
    
def blocks(step):
    return seq[step]

