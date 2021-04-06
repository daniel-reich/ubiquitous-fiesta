
def special_reverse_string(txt):
    a = list(txt)
    l=len(a)
    t=list("".join(txt.split() ))[::-1]
    ALF=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alf = list("abcdefghijklmnopqrstuvwxyz")
    ALFalf = ALF + alf
    b = []    
    for i in range(l):
        if a[0] == " ":
            b.append(" ")
        elif a[0] in ALF:        
            if t[0] in (ALFalf):
                b.append(t[0].upper())
                t = t[1:]
            elif not t[0] in (ALFalf):
                b.append(t[0])
                t = t[1:]
        else: 
            if t[0] in (ALFalf):
                b.append(t[0].lower())
                t = t[1:]
            elif not t[0] in (ALFalf):
                b.append(t[0])
                t = t[1:]              
        a = a[1:]
    return("".join(b))

