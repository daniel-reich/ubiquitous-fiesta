
def order_people(size,queue):
    final = []
    count = size[0] * size[1]
    #people = [x in range(1,queue+1)]
    row_count = 0
    column_count = 0
    index = 1
    if queue > count:
        return "overcrowded"
    if count >= queue:
    
        for row in range(1,size[0]+1):
            #if index <= queue:
                x = []
                
                if row_count % 2 == 0:
                    for item in range(0,size[1]):
                        if index <= queue:
                            x.append(index)
                        else:
                            x.append(0)
                        index += 1
                    final.append(x)
                        #column_count = size[1]
                    x = []
                if row_count % 2 != 0:
                    sub_index = index + size[1] -1
                    for item in range(0,size[1]):
                        if sub_index <= queue:
                            x.append(sub_index)
                        else:
                            x.append(0)
                        sub_index -= 1
                    final.append(x)
                    index += size[1]
                    x = []
                        #column_count = 0
                row_count += 1
            
    
        return final

