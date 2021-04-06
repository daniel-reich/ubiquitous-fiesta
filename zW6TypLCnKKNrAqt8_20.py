
def left_side(lst):
    result=[]
    for i in range(len(lst)):
        count=0
        for j in lst[:i]:
            if lst[i]>j:
                count+=1 
        result.append(count)
    return result
​
def right_side(lst):
    result=[]
    for i in range(len(lst)):
        count=0
        for j in lst[i:]:
            if lst[i]>j:
                count+=1 
        result.append(count)
    return result

