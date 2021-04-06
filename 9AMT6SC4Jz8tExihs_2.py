
def generate_nonconsecutive(n):
    ans = []
    for i in range(2**n):
        b = bin(i)[2:].zfill(n)
        if '11' not in b:
            ans.append(b)
    return ' '.join(ans)

