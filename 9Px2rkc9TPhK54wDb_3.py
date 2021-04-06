
def share(x,y):
    if x>y:
        for i in range(2,y+1):
            if x%i==0 and y%i==0:
                return True
        return False
    else:
        for i in range(2,x+1):
            if x%i==0 and y%i==0:
                return True
        return False
        
    
print(share(4,3)) 
def ecg_seq_index(x):
    s=[1,2]
    data=3
    while True:
        
        if x in s:
            return s.index(x)
        elif share(s[-1],data):
            if data not in s:
                s.append(data)
                data=3
            else:
                data+=1
        else:
            data+=1

