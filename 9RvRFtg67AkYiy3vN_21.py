
def left_rotations(txt):
    a=list(txt)
    b=[]
    b.append("".join(a))
    for i in range(len(a)-1):
        a.append(a.pop(0))
        b.append("".join(a))
    return(b)
  
​
def right_rotations(txt):
    a=list(txt)
    b=[]
    b.append("".join(a))
    for i in range(len(a)-1):
        a.insert(0,a.pop())
        b.append("".join(a))
    return(b)

