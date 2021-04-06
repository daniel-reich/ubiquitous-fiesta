
import re
​
def is_ladder_safe(lst):
    pc=0
    cc=0
    
    is_first_rung=True
    for l in lst:
​
        sizel=len(l)
       
        if  sizel<5:
            return False
        if len(re.findall("#",l))==sizel:
            if is_first_rung:
                is_first_rung=False
                cc=0
            else:
                
                if pc==0:
                    pc=cc
                    cc=0
                elif pc!=cc:
                    return False
                elif cc>3:
                    return False
                else:
                    cc=0
        elif len(re.findall("#",l))==2:
            if l[0]!="#" and l[4]!="#":
                return False
        else:
            return False
        cc+=1
​
    if is_first_rung:
        return False
    return True

