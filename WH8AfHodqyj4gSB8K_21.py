
def is_authentic_skewer(st):
    lst=[i for i in st]
    if lst[0].lower() and lst[-1].lower() not in "bcdfghjklmnpqrstvwxyz" or "-" not in lst: return False
    dashcount=0
    for n in range(1,len(lst)):
        if lst[n].isalpha()==False:dashcount+=1
        else:break
    lss=[lst[i] for i in range(0,len(lst),dashcount+1)]
    if '-' in lss or not all([lss[i].lower() not in "aeiou" for i in range(0,len(lss),2)]) or not all([lss[i].lower() in "aeiou" for i in range(1,len(lss),2)]):return False
    return True

