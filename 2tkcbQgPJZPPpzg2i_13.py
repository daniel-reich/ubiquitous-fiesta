
def sum_of_holes(N):
 r = [int(i) for u in range(1,N+1) for i in list(str(u))]
 return (r.count(0) + r.count(4) + r.count(6) + 2*r.count(8) + r.count(9))

