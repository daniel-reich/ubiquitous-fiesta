
def final_result(lst):
    while True:
        to_del_set=set()
        for index in range(0,len(lst)-1):            
            if lst[index]==lst[index+1]:
                jindex=index
                while jindex<len(lst) and lst[jindex]==lst[index] :
                    to_del_set.add(jindex)
                    jindex+=1
                break
        to_del_list=sorted(list(to_del_set),reverse=True)
        if not to_del_list:
            break
        for elem in to_del_list:
            lst.pop(elem)
    return lst

