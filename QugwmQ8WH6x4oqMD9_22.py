
def count_identical_lists(lst1, lst2, lst3, lst4):
    count=0
    if lst1==lst2:
        count+=1
    if lst1==lst3:
        count+=1
    if lst1==lst4:
        count+=1
    if lst2==lst3:
        count+=1
    if lst2==lst4:
        count+=1
    if lst3==lst4:
        count+=1
    if count==1:
        return 2
    else:
        return count

