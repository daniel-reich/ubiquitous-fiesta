
def almost_sorted(num_list):
    out_cast = []
    desc = []
    asc = []
    order = 0
    
    for number in range(0,len(num_list)):
        if number == 0:
            continue
        if number > 0:
            if num_list[number] - num_list[number-1] > 0:
                asc.append(number)
            if num_list[number] - num_list[number-1] < 0:
                desc.append(number)
    if len(desc) > len(asc):
        order = "descending"
    else:
        order = "ascending"
            
​
    if order == "ascending":     
        for index in range(0,len(num_list)):
            if index == 0:
                continue
            if index > 0:
                if num_list[index] > num_list[index-1]:
                    continue
                if num_list[index] < num_list[index-1]:
                    out_cast.append(num_list[index-1])
    
    if order == "descending": 
        for index in range(0,len(num_list)):
            if index == 0:
                continue
            if index > 0:
                if num_list[index] < num_list[index-1]:
                    continue
                if num_list[index] > num_list[index-1]:
                    out_cast.append(num_list[index])
    print(out_cast)
    if len(out_cast) == 1:
        return True
    else:
        return False

