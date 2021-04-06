
def final_countdown(lst):
    if not lst:
        return [0,lst]
    prev=lst[0]
    tmp=str(prev)
    for i,c in enumerate(lst[1:]):
        if c == prev-1:
            tmp=tmp+str(c)
        else:
            tmp=tmp+" "+str(c) 
        prev=c
    words=tmp.split(" ")
    lst1=[list(map(int,list(word))) for word in words if word[len(word)-1:] == "1"]
    return [len(lst1),lst1]

