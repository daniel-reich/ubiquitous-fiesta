
def mark_maths(lst):
    lst1=[]
    for i in lst:
        lst1.append(eval(i.replace("=","==")))
    return str(round((lst1.count(True)/len(lst))*100))+"%"

