
def is_authentic_skewer(s):
    v = ["A","E","I","O","U"]
    c = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
    if s[0] not in c or s[len(s)-1] not in c:
            #print("Beginning and end are not Consonents")
            return False
    nd=[x for x in s if x != "-"]
    for i in range(len(nd)-1):
        if (nd[i] in v and nd[i+1] in v) or (nd[i] in c and nd[i+1] in c):
            #print("No alternation between consonents and vowels")
            return False
    
    sp=s.index(nd[1])-s.index(nd[0])
    for i in range(0,len(s)-3,sp):
        if s[i] not in v and s[i] not in c:
            #print("Spacing Issue")
            return False
    return True

