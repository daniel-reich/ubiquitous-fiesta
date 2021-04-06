
def get_best_student(dic):
    lis = []
    for i in dic.values():
        l = []
        for j in i:
            l.append(j)
        avg = sum(l)//len(l)
        lis.append(avg)
    
    maxavg = max(lis)
    ind = lis.index(maxavg)
        
    l = 0
    for i in dic.keys():
        if(l == ind):
            return i
            break
        else:
            l+=1 
get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
})

