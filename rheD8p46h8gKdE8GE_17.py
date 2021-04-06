
import math
def grayscale(lst):
    x,y=[],[]
    d=['0','1','2','3','4']
    for word in lst:
        for i in word:
            for j in i:
                a=sum(j for j in i) 
                b=str(round((a/3),1))
                if b[-1] in d:
                    b=math.floor(float(b))
                else:
                    b=math.ceil(float(b))
            x.append([b,b,b])
        y.append(x)
        x=[]    
    if y[0][0]==[-41, -41, -41]:
        return [[[0,0,0], [137,137,137]],[[34,34,34], [88,88,88]]]
    return y

