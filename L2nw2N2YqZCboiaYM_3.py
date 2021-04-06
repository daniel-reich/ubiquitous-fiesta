
def repeated(s):
    return any(len(s)%size == 0 and s[0:size]*(len(s)//size) == s for size in range(len(s)//2, 1, -1))

