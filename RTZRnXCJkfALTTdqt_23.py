
def sum_neg(lst):
    if lst == []:
        return []
    else:
        newlst = [i for i in lst if i < 0]
        newlst1 =[i for i in lst if i > 0]
        return [len(newlst1),sum(newlst)]

