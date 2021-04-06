
def convert_to_hex(txt):
        list(txt)
        l=[]
        s=""
        for i in range(0,len(txt)):
            l.append(hex(ord(txt[i]))[2:])
        for i in range(0,len(l)):
            s+=l[i]+" "
        
        return s[:len(s)-1]

