
def num_then_char(lst):
​
    unpck_lst = [ea for each in lst for ea in each]
    full_lst = sorted([x for x in unpck_lst if type(x) == int or type(x) == float])\
                + sorted([x for x in unpck_lst if type(x) == str])
    temp = 0
    final = []
    for each in lst:
        final.append(full_lst[temp:len(each)+temp])
        temp += len(each)
        
    return final

