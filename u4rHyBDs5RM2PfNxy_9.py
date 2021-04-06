
def count_ones(lst):
    count=0
    lst="".join(map(str,lst))
    lst1=lst.split("0")
    for i in lst1:
        if len(i)>1:
            count+=1
    return count

