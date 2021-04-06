
def left_slide(row):
    row1=row[:]
    while 0 in row1:
        row1.remove(0)
    lst=[]
    n1=len(row1)
    i=0
    while True:
        if i >n1-1:
            break
        elif i==n1-1:
            lst.append(row1[i])
            break
        elif row1[i]==row1[i+1]:
            num=row1[i]*2
            lst.append(num)
            i+=2
        else:
            lst.append(row1[i])
            i+=1
    n2=len(lst)
    n3=len(row)
    for i in range(0,n3-n2):
        lst.append(0)
    return lst

