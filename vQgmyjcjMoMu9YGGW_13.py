
def simplify(txt):
    a, b = int(txt.split("/")[0]), int(txt.split("/")[1])
    
    for i in range(max(a, b), 1, -1):
        if (a % i == 0) and (b % i == 0):
            a /= i
            b /= i
    
    return str(int(a)) + "/" + str(int(b)) if b!= 1 else str(int(a))

