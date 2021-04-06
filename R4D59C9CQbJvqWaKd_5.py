
def batting_avg(lst):return str(round(sum(list(map(lambda x:x[0],lst)))/sum(list(map(lambda x:x[1],lst))),3))[1:].ljust(4,'0')

