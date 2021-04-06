
def is_valid(s):
    d = {item:s.count(item)for item in s}
    lst = sorted(d.values())
    n = [lst[0]]
    count = 0
    for i in range(1,len(lst)):
        if lst[i] == n[-1]:
            n.append(lst[i])
            
        else:
            if max(lst[i],n[-1])-min(lst[i],n[-1]) == 1:
                count+=1
                
            else:
                return 'NO'
   
    if count == 0 or count == 1:
        return 'YES'
​
    else:
        return 'NO'

