
def get_gcd(a, b):
    while b:
        a, b = b, a%b
    return a
​
def ecg_seq_index(n):
    seq = [2]
    while seq[-1] != n:
        i = 2
        while get_gcd(i, seq[-1]) == 1 or i in seq:
            i += 1
        seq.append(i)
    return len(seq)

