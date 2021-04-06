
import math
def pyramidal_string(string, _type):
    x=1+8*len(string)
    if(math.sqrt(x).is_integer()):
        arr=[]
        lb=0;
        ub=1;
        c=2;
        if("REG"==_type):
            while(len(string)>=ub):
                arr.append(" ".join(string[lb:ub]))
                lb=ub
                ub=lb+c
                c=c+1
        else:
            c=int((math.sqrt(x)-1)*0.5);
            ub=c
            while(c>=1):
                    arr.append(" ".join(string[lb:ub]))
                    c=c-1
                    lb=ub
                    ub=lb+c
        return arr;
                
    else:
        return "Error!"

