
def pairs(lst):
    result  = [[lst[i],lst[-i+-1]] for i in range(0,len(lst)//2)]
    if len(lst)%2!=0:
        result.append([lst[len(lst)//2],lst[len(lst)//2]])
        
    return result

