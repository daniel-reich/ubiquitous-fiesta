
def product(lst):
    lst_ = list(set(lst))
    
    if len(lst_) == 1:
        return lst_[0] * lst_[0] 
    
    else:
        lst_.sort()
        return lst_[-1] * lst_[-2]

