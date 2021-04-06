
def josephus(n, k):
    return 1 if n==1 else 1 +(josephus(n-1, k) +k -1)%n

