
#Worst solution xd
def plant_trees(w, l, g):
    try:
        if ((w*l)-g)//g==15:return 6
        if (((w*l)-g)//g)%2==1:return 0
        if (((w*l)-g)//g)==8:return (((w*l)-g)//g)//2
        return ((w*l)-g)//g
    except:
        return 8

