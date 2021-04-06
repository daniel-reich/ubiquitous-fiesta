
def flip_list(lst):
    empty = []
    for i in lst:
        if isinstance(i,int):
            empty.append([i])
              
        elif isinstance(i,list):
            for x in lst:
                for y in x:
                    empty.append(y)
            return empty    
        elif lst == []:
            return empty
    return empty

