
def shuffle_count(num):
    lst = list(range(1,num+1))
    count = 0
    new_list = []
    pos = [i for i in range(len(lst)) if i%2!=0]
    while True:
        newlist = lst[:len(lst)//2]
        for i in range(len(pos)):
            newlist.insert(pos[i],lst[len(lst)//2:][i])
            
        count+=1
        if newlist == list(range(1,num+1)):
            return count
        else:
            lst = newlist

