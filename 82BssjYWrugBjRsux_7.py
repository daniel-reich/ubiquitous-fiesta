
def index_multiplier(lst):
    if len(lst) == 0:
        return 0
    a = 0
    overall = 0
    for i in lst:
        overall = overall + a*i
        a+=1
    return overall

