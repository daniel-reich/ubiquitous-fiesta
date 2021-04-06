
def generate_palindromes(limit):
    k = []
    for i in range(0,limit+1):
        i=str(i)
        j = i[::-1]
        if i==j:
            k.append(int(i))
    l=len(k)-15
    for i in range(0,l,1):
        i=i-i
        k.remove(k[i])
    return k

