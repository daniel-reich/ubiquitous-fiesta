
def is_ascending(s,start=True,size=0):
    if len(s)==0:
        return True
    if start:
        for length in range(1,len(s)//2+1):
            if length>len(s)-length:
                return False
            else:
                if int(s[:length])+1==int(s[length:2*length]):
                    if is_ascending(s[length:],start=False,size=length)==False:
                        continue
                    else:
                        return True
        return False
    else:
        if size>len(s)-size:
            if size-len(s)==0:
                return True
            else:
                return False
        else:
            if int(s[:size])+1==int(s[size:2*size]):
                return is_ascending(s[size:],start=False,size=size)
            else:
                return False

