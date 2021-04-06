
def ordered_matrix(a, b):
    i = 0
    temp = []
    array = []
    for y in range(a):
        for x in range(b):            
            i += 1
            temp.append(i)        
        array.append(temp)
        temp = []
    return array

