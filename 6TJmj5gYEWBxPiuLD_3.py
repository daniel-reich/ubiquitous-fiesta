
def combinations(classroom):
    comb_list = []
    for desk_id in range(0, len(classroom)):
        #print ("Checking desk number: {}".format(desk_id))
        if classroom[desk_id] != "#": #if already occupied we skip
            #print ("Checking desk number: {}".format(desk_id))
            if desk_id == 0: #check to the right and below only
                #print ("Checking desk number 1")
                if classroom[desk_id+1] == "0": #check to the right
                    comb_list.append([desk_id+1, desk_id+2])
                if classroom[desk_id+2] == "0": #check below
                    comb_list.append([desk_id+1, desk_id+3])
            elif desk_id == 1: #check to the left and below only
                if classroom[desk_id-1] == "0": #check to the left
                    if [desk_id, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id])
                if classroom[desk_id+2] == "0": #check below
                    comb_list.append([desk_id+1, desk_id+2])
            elif desk_id == len(classroom)-2: #check to the right and above only
                if classroom[desk_id+1] == "0": #check to the right
                    comb_list.append([desk_id+1, desk_id+2])
                if classroom[desk_id-2] == "0": #check above
                    if [desk_id-1, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id-1])
            elif desk_id == len(classroom)-1: #check to the left and above only
                if classroom[desk_id-1] == "0": #check to the left
                    if [desk_id, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id])
                if classroom[desk_id-2] == "0": #check above
                    if [desk_id-1, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id-1])
            #for everything else check above, below and left (for even) and right (for odd)
            else:
                if classroom[desk_id-2] == "0": #check above
                    if [desk_id-1, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id-1])
                if classroom[desk_id+2] == "0": #check below
                    if [desk_id+3, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id+3])
                if (desk_id+1)%2 == 0: #check to the left
                    if classroom[desk_id-1] == "0":
                        if [desk_id, desk_id+1] not in comb_list:
                          comb_list.append([desk_id+1, desk_id])
                else: #check to the right
                    if classroom[desk_id+1] == "0":
                        comb_list.append([desk_id+1, desk_id+2])
​
    return (comb_list)
        
            
​
def seating_students(lst):
    desks = int(lst[0])
    classroom = []
    for x in range(0, desks):
        if (x+1) in lst[1:]:
            classroom.insert(x, "#")
        else:
            classroom.insert(x, "0")
    return len(combinations(classroom))

