
def accumulating_list(lst):
    sum=0
    sum_list=[]
    for a in lst:
        sum+=a
        sum_list.append(sum)
    return sum_list

