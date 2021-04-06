
import math
def encryption(txt):
    txt=txt.replace(" ","")
    print(len(txt))
    r=round(math.sqrt(len(txt)))
    c=math.ceil(math.sqrt(len(txt)))
    
    coords=[str(i)+str(j) for i in range(r) for j in range(c)]
    dict1=dict(zip(coords,txt))
    print(dict1)
    lst=[]
    for i in range(r+1):
        tmp=""
        for j in range(c+1):
            if str(j)+str(i) in dict1:
                tmp=tmp+(dict1[str(j)+str(i)])
        lst.append(tmp)
    print(" ".join(lst))    
    return " ".join(lst).strip()

