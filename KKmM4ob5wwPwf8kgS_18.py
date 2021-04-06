
def get_frequencies(lst):
    dict_ = dict()
    if len(lst) ==0:
        return {}
    else:
        for i in lst:
            if i in dict_:
                dict_[i]+=1
            else:
                dict_[i]= 1
        return dict_

