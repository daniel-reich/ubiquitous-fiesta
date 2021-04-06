
def last_ancestor(folders, X, Y):
    in_y=[]
    def is_it_inside(folders, X, Y):
        in_y=[]
        try:
            for i in range(len(folders[Y])):
                in_y+=folders[Y][i]
                useless_var=0
        except KeyError:
            return X==Y
        for i in range(len(folders[Y])):
            in_y2=in_y
            in_y=[]
            for j in range(len(in_y2)):
                try:
                    in_y+=folders[in_y2[j]]
                except KeyError:
                    useless_var=0
            in_y+=in_y2+[Y]
        return X in in_y
    def all_files(folders):
        result=[]
        for i in folders:
            result+=i
            try:
                for j in range(len(folders[i])):
                    result+=folders[i][j]
            except IndexError:
                useless_var=0
        return result
    x_in=[]
    y_in=[]
    every_file=list(dict.fromkeys(all_files(folders)))
    for i in every_file:
        if is_it_inside(folders, X, i):
            x_in+=i
    for i in every_file:
        if is_it_inside(folders, Y, i):
            y_in+=i
    x_in_set=set(x_in)
    both_in_set=x_in_set.intersection(y_in)
    both_in=list(both_in_set)
    while len(both_in)!=1:
        both_in_ele_0=both_in[0]
        both_in.remove(both_in[0])
        for j in both_in:
            if is_it_inside(folders,both_in_ele_0,j):
                both_in.remove(j)
        both_in.append(both_in_ele_0)
    return both_in[0]
    return both_in[0]

