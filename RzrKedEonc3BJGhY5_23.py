
def plant_trees(w, l, g):
    if g == 0:
        return w*l-1;
    elif g > w*l:
        return 0;
    elif g == 2:
        return 0
    else:
        p = ((w+l)*2)-2;
        L=[];
        for i in range(0,p,g+1):
            L.append("O")
        return L.count("O")-1;

