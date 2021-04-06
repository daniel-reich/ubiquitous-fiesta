
def overlapping_rectangles(r1, r2):
    l1,l2 = sorted([r1,r2],key=lambda x: x[0])
    m1,m2 = sorted([r1,r2],key=lambda x: x[1])  
    x = min(l1[2]-(l2[0]-l1[0]),l2[2]) if l2[0]-l1[0]<l1[2] else 0
    y = min(m1[3]-(m2[1]-m1[1]),m2[3]) if m2[1]-m1[1]<m1[3] else 0
    return x*y

