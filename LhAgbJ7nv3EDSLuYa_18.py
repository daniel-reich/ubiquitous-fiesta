
seq = [0] * 1001
seq[1] = 1
for i in range(1, 1000):
    seq[i + 1] = 1 + seq[i + 1 - seq[seq[i]]]
​
def golomb(n):
    return seq[1:n+1]

