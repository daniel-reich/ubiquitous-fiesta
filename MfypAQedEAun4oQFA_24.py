
def perrin(n):
    seq_perrin = []
​
    seq_perrin.append(3)
    seq_perrin.append(0)
    seq_perrin.append(2)
​
    if n == 2 or n==1 or n==0:
        return seq_perrin[n]
​
    if n > 2:
        for i in range(3, n + 1):
            seq_perrin.append(seq_perrin[i-2] + seq_perrin[i-3])
​
​
    return (seq_perrin[-1])

