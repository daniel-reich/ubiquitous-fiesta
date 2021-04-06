
def cleave(string, lst):
    lst=sorted(lst,key=len,reverse=True)
    max_count=[string.count(x) for x in lst]
    i=0
    dict1={}
    while(i<max(max_count)):
        for x in lst:
            if x in string and len(x)>1:
                y=[x,string.find(x)]
                dict1[string.find(x)]=x
                string=string[:string.find(x)+len(x)].replace(string[string.find(x):(string.find(x)+len(x))],'1234567890'[:len(x)])+string[string.find(x)+len(x):]
        i+=1
    i=0
    while(i<max(max_count)):
        for x in lst :
            if x in string:
                y=[x,string.find(x)]
                dict1[string.find(x)]=x
                string=string[:string.find(x)+len(x)].replace(string[string.find(x):(string.find(x)+len(x))],'1234567890'[:len(x)])+string[string.find(x)+len(x):]
        i+=1          
    l1=[dict1[x] for x in sorted(dict1)]
    if len("".join(l1))==len(string):
        return (" ".join(l1))    
    else:
        return ("Cleaving stalled: Word not found")

