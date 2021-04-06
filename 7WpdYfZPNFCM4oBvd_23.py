
def is_magic(square):
        a=len(square)
        i,j,c,d,e,t,t1,t2=0,0,0,0,0,[],[],[]
        if a==0:
                return True
        elif a==1 and (square[0]!=[1]):
                return False
        else:
                b=sum(square[0])
        if b>(a+a**3)/2:
                return False
        while i<a:
                if len(square[i])!=a or sum(square[i])!=b:
                        return False
                else:
                        i+=1
        while j<a:
                while c<a:
                        t.append(square[c][j])
                        c+=1
                if sum(t)!=b:
                        return False
                else:
                        j+=1
        while d<a:
                while e<a:
                        t1.append(square[d][e])
                        t2.append(square[d][a-e-1])
                        d+=1
                        e+=1
        if sum(t1)!=b or sum(t2)!=b:
                return False
        return True

