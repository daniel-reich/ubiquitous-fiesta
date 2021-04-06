
def special_reverse_string(txt):
    caps=[i for i,c in enumerate(txt) if c.isupper()]
    spaces=[i for i,c in enumerate(txt) if c==" "]
    str1="".join(txt.lower().split(" "))
    str2=str1[::-1]
    str3=""
    j=0
    for i,x in enumerate(str2):
        if j in spaces:
            j+=1
            str3=str3+" "+x
        else:
            str3=str3+x
        j+=1
    return "".join([x.upper() if i in caps else x for i,x in enumerate(str3) ])

