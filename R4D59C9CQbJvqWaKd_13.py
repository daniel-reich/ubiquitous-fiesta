
def batting_avg(lst):
    a = round((sum(i for i,j in lst)/sum(j for i,j in lst)),3)
    s = str(a).ljust(5,'0').lstrip('0')
    return s

