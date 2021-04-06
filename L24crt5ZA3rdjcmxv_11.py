
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
    
    
    n=person["name"].lower()
    s=person["surname"].lower()
    g=person["gender"]
    d=person["dob"].split("/")
    
    nn, ss, gg, mscn,mscs = [], [], [], [], []
    cnst="zrtypqsdfghjklmwxcvbn"
​
    
    for i in n:
        if i in cnst:
            nn.append(i)
        else:
            mscn.append(i)   
    if len(nn)>3:
        fnn = (nn[0]+nn[2]+nn[3]).upper()
    elif len(nn)==3:
        fnn = (nn[0]+nn[1]+nn[2]).upper()
    elif len(nn)<2:
        fnn = (nn[0]+mscn[0]+"X").upper()        
    elif len(nn)<3:
        fnn = (nn[0]+nn[1]+mscn[0]).upper()        
    for i in s:
        if i in cnst:
            ss.append(i)
        else:
            mscs.append(i)
    if len(ss)>3:
        fss = (ss[0]+ss[2]+ss[3]).upper()
    elif len(ss)==3:
        fss = (ss[0]+ss[1]+ss[2]).upper()
    elif len(ss)<2:
        fss = (ss[0]+mscs[0]+"X").upper()                
    elif len(ss)<3:
        fss = (ss[0]+ss[1]+ mscs[0]).upper()        
    
    fdy = d[2][-2:]
    fdm = months[d[1]]
    
    if g == "F":
        fdd = str(40+int(d[0]))
    if g == "M":
        if int(d[0]) < 10:
            fdd = "0"+d[0]
        else:
            fdd = d[0]
        
​
    
    return (fss+fnn+fdy+fdm+fdd)

