
def landscape_type(lst):
    r=''
    for i in range(len(lst)-1):
        if lst[i+1]>lst[i]:r+='+'
        if lst[i+1]<lst[i]:r+='-'
        if lst[i+1]==lst[i]:r+='e'
    if r.count('+-')==1 and r[0]!='-':
        return 'mountain'
    if r.count('-+')==1 and r[-1]!='-':
        return 'valley'
    return 'neither'

