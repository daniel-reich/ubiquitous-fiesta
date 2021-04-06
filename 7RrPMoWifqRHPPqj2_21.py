
def safecracker(a,lst):
    numbers_list=[]
    numbers_list.append((a-lst[0])%100)
    numbers_list.append((numbers_list[0]+lst[1])%100)
    numbers_list.append((numbers_list[1]-lst[2])%100)
    return(numbers_list)

