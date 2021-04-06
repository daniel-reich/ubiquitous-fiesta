
def overlapping_rectangles(rect1, rect2):
    x,y=0,0
    if rect1[0]<rect2[0]:L,R=rect1,rect2   
    else:R,L=rect1,rect2 
    if L[0]+L[2]>=R[0]:x=min(L[0]+L[2],R[0]+R[2])-max(L[0],R[0])
    if L[1]<=R[1] and L[1]+L[3]>R[1] or L[1]>=R[1] and R[1]+R[3]>L[1]:
        y=min(R[1]+R[3],L[1]+L[3])-max(L[1],R[1])
    return x*y

