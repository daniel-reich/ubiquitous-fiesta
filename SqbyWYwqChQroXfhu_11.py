
def lower_triang(arr):
    for i, sublist in enumerate(arr):
        sublist[i+1:]=[0]* len(sublist[i+1:])
        
    return arr

