
def P(a,b):
    if a[1]=="2" and a[0]==b[0] and b[1]=="4":
        return True
    elif  (not a[1]=="1") and a[0]==b[0] and b[1]==str(int(a[1])+1):
        return True
    return False
        
    
def K(a,b):
    d={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    if a==b:
        return False
    return abs(d[a[0]]-d[b[0]])<=1 and abs(int(a[1])-int(b[1]))<=1
    
    
def B(a,b):
    d={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    if a==b:
        return False
    return abs(d[a[0]]-d[b[0]])==abs(int(a[1])-int(b[1]))
    
def R(a,b):
    d={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    if a==b:
        return False
    if a[0]==b[0] or a[1]==b[1]:
        return True
    return False
    
def Q(a,b):
    d={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    if B(a,b) or R(a,b):
        return True
    return False
    
def K1(a,b):
    d={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    if abs(d[a[0]]-d[b[0]])==1 and abs(int(a[1])-int(b[1]))==2:
        return True
    if abs(d[a[0]]-d[b[0]])==2 and abs(int(a[1])-int(b[1]))==1:
        return True
    return False
    
    
​
def can_move(piece, current, target):
        d={ "Pawn":0, "Knight":1, "Bishop":2, "Rook":3\
            ,"Queen":4, "King":5}
        if d[piece]==0:
            return P(current, target)
        elif d[piece]==1:
            return K1(current, target)
        elif d[piece]==2:
            return B(current, target)
        elif d[piece]==3:
            return R(current, target)
        elif d[piece]==4:
            return Q(current, target)
        else :
            return K(current, target)

