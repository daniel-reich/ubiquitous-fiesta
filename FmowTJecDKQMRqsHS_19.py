
def crop_hydrated(field):
    
    a= len(field)
    b= len(field[0])    
    c,w,d=[],[],[]
    for i in range(a):
        for j in range(b):
            if field[i][j] == "c":
                c.append("c")
            elif field[i][j]=="w":
                w.append("w")
    if len(c) == 0 or len(w)== 0:   
        return False
    for i in range(a):
        for j in range(b):
            
            if field[i][j] == "c":
                d=[]
                if ((i+1)<(a)):
                    if field[i+1][j] == "w":
                        d.append(1)
                if ((j+1)<(b)) and ((i+1)<(a)):
                    if field[i+1][j+1] == "w":
                        d.append(1)
                if ((j+1)<(b)):
                    if field[i][j+1] == "w":
                        d.append(1)
                if (((j+1)<(b)) and ((i-1)>0))  :
                    if field[i-1][j+1] == "w":
                        d.append(1)
                if ((i-1)>-1):
                    if field[i-1][j] == "w":
                        d.append(1)
                if (((i-1)>-1) and ((j-1)>-1))  :
                    if field[i-1][j-1] == "w":
                        d.append(1)
                if ((j-1)>-1):
                    if field[i][j-1] == "w":
                        d.append(1) 
                if  ((i+1)<a) and (j-1>-1):
                    if field[i+1][j-1] == "w":
                        d.append(1)
                if len(d) == 0:
                    return False
    return True

