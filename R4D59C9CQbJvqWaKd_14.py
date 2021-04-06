
def batting_avg(lst):
    return str(round(sum(a for a,b in lst)/float(sum(b for a,b in lst)),3))[1:].ljust(4,"0")

