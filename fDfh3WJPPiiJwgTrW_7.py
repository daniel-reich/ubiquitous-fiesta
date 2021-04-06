
def num_of_sublists(lst): 
    count = 0
    for el in lst:
        if type(el)== type([]): 
            count+= 1
              
    return count

