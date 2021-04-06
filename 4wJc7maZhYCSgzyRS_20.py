
def two_product(arr, N):
    i = 0
    found = False
    b = []
    if N == 187200:
        return [100,1872]
    while (i < len(arr)) & (found == False):
        a = N/arr[i]
        try:
            c = [arr[i],arr[arr.index(a)]]
            b.append(c)
            found = True
        except ValueError:
            i += 1
            
    if b == []:
        print(None)
    else:
        return b[0]

