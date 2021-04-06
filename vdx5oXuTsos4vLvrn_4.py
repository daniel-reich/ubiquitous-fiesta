
def is_kaprekar(n):
    sq = str(n**2)
    L = len(sq)
    if L == 1:
        return n == 1
    a = int(sq[:L // 2])
    b = int(sq[L // 2:])
    return n == a + b
​
kaprekar = set([k for k in range(1, 10**5) if is_kaprekar(k)])
​
def kaprekar_numbers(p, q):
    ans = [k for k in range(p, q + 1) if k in kaprekar]
    return "INVALID RANGE" if len(ans) == 0 else ' '.join(map(str, ans))

