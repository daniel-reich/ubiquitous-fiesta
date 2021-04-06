
def closing_in_sum(luku):
    
    nums = []
    luku = str(luku)
    
    start = 0
    end = len(luku) - 1
    while start <= end:
        if start == end:
            nums.append(luku[start])
        else:
            nums.append(luku[start]+luku[end])
        start+=1
        end-=1
    
    result=0
    for i in nums:
        result+=int(i)
    return result

