
def get_quartiles(lst, method):
    
    a=sorted(lst)
    q0, q4 = a[0], a[-1]
    if len(a)%2==1: q2 = a[(len(a)-1)//2]
    else: q2 = (a[len(a)//2] + a[(len(a)//2)-1])/2
​
    if method == "T":
        if len(a)%2==1:
            b1 = a[:(len(a)+1)//2]
            b2 = a[(len(a)+1)//2-1:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2            
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2                 
        else:
            b1 = a[:(len(a)+1)//2]
            b2 = a[(len(a)+1)//2:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2 
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2        
​
    elif method == "MM":
        if len(a)%2==1:
            b1 = a[:(len(a)-1)//2]
            b2 = a[(len(a)+1)//2:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2            
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2                 
        else:
            b1 = a[:(len(a)+1)//2]
            b2 = a[(len(a)+1)//2:]
            if len(b1)%2==1: q1 = b1[(len(b1)-1)//2]
            else: q1 = (b1[len(b1)//2] + b1[(len(b1)//2)-1])/2 
            if len(b2)%2==1: q3 = b2[(len(b2)-1)//2]
            else: q3 = (b2[len(b2)//2] + b2[(len(b2)//2)-1])/2  
                    
    elif method == "MS":
        if ((len(a)+1)/4)-((len(a)+1)//4) < 0.5:
            q1 = a[int((len(a)+1)//4)-1]
            q3 = a[3*(len(a)+1)//4]
        else: # ((len(a)+1)/4)-((len(a)+1)/4) < 0.5:
            q1 = a[int((len(a)+1)//4)]
            q3 = a[3*(len(a)+1)//4-1]
                                        
    return ([q0,q1,q2,q3,q4])

