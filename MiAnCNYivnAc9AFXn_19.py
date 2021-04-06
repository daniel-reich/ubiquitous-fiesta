
def changeTypes(lst):
    x=[]
    for i in lst:
        if(type(i) ==str):
            i=i+"!"
            i= i.capitalize()
           
            x.append(i)
        elif(type(i)==bool):
            if(i==True):
                i=False
                x.append(i)
            else:
                i=True
                x.append(i)
        if(type(i)==int):
            if(i%2==0):
                i=i+1
                x.append(i)
            else:
                x.append(i)
​
    return x

