
import itertools
def next_number(num):
    if len(str(num))==1:return num
    l=[ x for x in str(num)]
    l2=[]
    for i in itertools.permutations(l,len(l)):
        if int("".join(list(i)))>num:l2.append(int("".join(list(i))))
    l2.sort()
    if len(l2)==0:return num
    return l2[0]

