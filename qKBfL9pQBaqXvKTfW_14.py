
def sum_of_slices(lst):
    lst_total=[]
    total=0
    for num in lst:
        if total+num<100:
            total+=num
        elif total+num>100:
            lst_total.append(total)
            total=num
        else:
            lst_total.append(100)
            total=0
        
    return lst_total +[total]

