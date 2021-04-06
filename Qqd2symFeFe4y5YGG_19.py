
def palindromic_date(date):
    data1 = date.replace("/","")
    data2= data1[2:4]+data1[:2]+data1[4:]
    i = 0
    j = len(data1)-1
    while i <=j:
        if data1[i]!=data1[j] or data2[i]!=data2[j]:
            return False
        i+=1
        j-=1
    return True

