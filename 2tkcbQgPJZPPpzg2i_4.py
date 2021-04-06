
def sum_of_holes(N):
    s = "".join(map(str,range(1,N+1)))
    return sum(s.count(i) for i in "0469") + s.count("8")*2

