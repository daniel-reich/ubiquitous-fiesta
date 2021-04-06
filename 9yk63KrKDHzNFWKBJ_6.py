
def is_it_inside(f,x,y):
    if x==y:return True
    l = f.get(y)
    try:
     if x in l:return True
    except:
        return False
    for i in l:
        if i in f.keys():
            l2=[j for j in f.get(i)]
            if x in l2:return True
            for k in l2:
              if k in f.keys():
                 if x in f.get(k):return True
    return False

