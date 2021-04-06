
def collect(s, n):
    return sorted(''.join(s[n*index:n*index+n]) for index in range(len(s)//n))

