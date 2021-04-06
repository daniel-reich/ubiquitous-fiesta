
def sums_of_powers_of_two(n):
    n =bin(n)[2::][::-1]
    return [2**(int(i)) for i in range(len(n)) if n[i]=='1']

