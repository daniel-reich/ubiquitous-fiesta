
def can_patch(bridge, planks):
    dictionary = {}
    count = []
    end_dict = []
    for index in range(0,len(bridge)):
        if index == 0:
            if bridge[index+1] == 0 and bridge[index] == 0:
                count.append(bridge[index])
            else:
                continue
        if index == len(bridge) - 1:
            if bridge[index] == 0 and bridge[index-1] == 0:
                count.append(bridge[index])
                if count is not None and len(count) > 1:
                    dict_length = [x for x,y in dictionary.items()] 
                    if len(count) not in dict_length:
                        dictionary[len(count)] = 1
                    if len(count) in dict_length:
                        dictionary[len(count)] += 1
            if bridge[index] != 0:
                if count is not None and len(count) > 1:
                    dict_length = [x for x,y in dictionary.items()] 
                    if len(count) not in dict_length:
                        dictionary[len(count)] = 1
                    if len(count) in dict_length:
                        dictionary[len(count)] += 1
                
        if index != 0 and index != len(bridge)-1:
​
            if bridge[index+1] == 0 and bridge[index] == 0:
                count.append(bridge[index])
            if bridge[index+1] != 0 and bridge[index] == 0 and bridge[index-1] == 0:
                count.append(bridge[index])
            if bridge[index] != 0:
                if count is not None and len(count) > 1:
                    dict_length = [x for x,y in dictionary.items()] 
                    if len(count) not in dict_length:
                        dictionary[len(count)] = 1
                    if len(count) in dict_length:
                        dictionary[len(count)] += 1
                    count = []
                if count is None:
                    continue
​
    for x,y in dictionary.items():
        if x in planks or (x-1) in planks:
            if planks.count(x) >= y or planks.count(x-1) >= y:
                end_dict.append(x)
        else:
            continue
    check = [x for x,y in dictionary.items()]
    if len(end_dict) == len(check):
        return True
    else:
        return False

