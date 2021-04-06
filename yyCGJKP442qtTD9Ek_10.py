
def sums_of_powers_of_two(n):
    b = bin(n)[2:][::-1]
    p = 1
    ans = []
    for bit in b:
        if bit == '1':
            ans.append(p)
        p *= 2
    return ans

