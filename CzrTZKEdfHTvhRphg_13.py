
def gcf(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcf(b,a%b) 
 
def mixed_number(Input):
    top = ''
    if Input[0]=="-":
        pos = "-"
    else:
        pos = ""
​
    for i in Input:
        if i == '/':
            break
        top+=i
    bottom = ''
    for i in Input[len(top)+1:]:
        if i == '/':
            break
        bottom+=i
        
    bottom = int(bottom)
    top = abs(int(top))
    if top//bottom == top/bottom:
        return pos + str(top//bottom) 
    else:
        Gcf = gcf(top,bottom)
        if str(top//bottom) == "0":
                return pos +str(int((top/Gcf)%(bottom/Gcf)))+"/" + str(int(bottom/Gcf))
        return pos + str(top//bottom) + ' ' + str(int((top/Gcf)%(bottom/Gcf)))+"/" + str(int(bottom/Gcf))

