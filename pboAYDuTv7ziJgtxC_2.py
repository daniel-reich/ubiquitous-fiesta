
def min_turns(orig,new):
    new_list = []
    #go from 0-9
    for i in range(0,len(orig)):
        x = int(orig[i])
        y = int(new[i])
        new_list.append(min(abs(x-y),10-abs(x-y)))
    return sum(new_list)
print(min_turns("1111","1100")) #should return 9
#1 + 4 + 1 + 3

