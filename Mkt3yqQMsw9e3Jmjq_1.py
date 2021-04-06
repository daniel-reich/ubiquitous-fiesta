
def disjoint_cycle_form(per_list):
    length = len(per_list)
    
    processed = []
    
    result = set()
    while len(processed) != length:
​
        for i in range(length):
            if i not in processed:
​
                next_ele = i
                working_list = []
                working_list.append(i)
                processed.append(i)
                next_ele = per_list[i]
                while(next_ele not in working_list):
                    working_list.append(next_ele)
                    processed.append(next_ele)
                    next_ele = per_list[next_ele]
                
                if len(working_list) != 1:
                    result.add(tuple(working_list))
    
    return result

