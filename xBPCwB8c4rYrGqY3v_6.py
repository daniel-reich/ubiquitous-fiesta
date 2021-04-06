
def missing(lst):
    step = (max(lst)-min(lst))/len(lst)
    return list(set([min(lst)+step*i for i in range(1,len(lst)+1)])-set(lst))[0]

