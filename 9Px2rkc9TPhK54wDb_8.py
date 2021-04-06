
def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
​
​
def ecg_seq_index(n):
    ecg = [1, 2]
    while ecg[-1] != n:
        k = 3
        while k in ecg or gcd(ecg[-1], k) == 1:
            k += 1
        ecg.append(k)
    return len(ecg) - 1

