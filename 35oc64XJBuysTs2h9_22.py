
def mediane(l):
    l.sort()
    mod = (len(l)%2)
    if mod == 1:
        #median is the len(l)%2)th element
        median = l[int(len(l)/2)]
    else:
        #median is between the (len(l)%2)th element and the (len(l)%2 -1)th element
        median = (l[int(len(l)/2)]+l[int(len(l)/2)-1])/2.0
    return [[e for e in l[:int(len(l)/2)]] , [e for e in l[int(len(l)/2)+mod:]]], median
​
def turkey(lst):
    lst.sort()
    Q0 = lst[0]
    Q4 = lst[-1]
    halfed,Q2 = mediane(lst)
    if len(lst)%2 == 1:
        #odd situation, turkey method inculdes the median into upper && lower brackets
        halfed[0].reverse()
        halfed[0].append(Q2)
        halfed[0].reverse()
        halfed[1].append(Q2)
    Q1 = mediane(halfed[0])[1]
    Q3 = mediane(halfed[1])[1]
    return [Q0,Q1,Q2,Q3,Q4]
​
def MM(lst):
    lst.sort()
    Q0 = lst[0]
    Q4 = lst[-1]
    halfed,Q2 = mediane(lst)
    Q1 = mediane(halfed[0])[1]
    Q3 = mediane(halfed[1])[1]
    return [Q0,Q1,Q2,Q3,Q4]
​
def MS(lst):
    lst.sort()
    Q0 = lst[0]
    Q4 = lst[-1]
    Q2 = mediane(lst)[1]
    inc_Q1 = (len(lst)+1)/4
    inc_Q3  = inc_Q1*3
    if inc_Q1-float(int(inc_Q1))>=0.5:
        inc_Q1 = int(inc_Q1) +1
    else:
        inc_Q1 = int(inc_Q1)
​
    if inc_Q3-float(int(inc_Q3))>0.5:
        inc_Q3 = int(inc_Q3) +1
    else:
        inc_Q3 = int(inc_Q3)
    return [Q0,lst[inc_Q1-1],Q2,lst[inc_Q3-1],Q4]
​
​
def get_quartiles(lst,method):
    if method == 'T':
        return turkey(lst)
    if method =='MM':
        return MM(lst)
    if method == 'MS':
        return MS(lst)

