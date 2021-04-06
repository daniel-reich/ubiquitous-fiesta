
def count_identical_lists(lst1, lst2, lst3, lst4):
   total = [lst1,lst2,lst3,lst4]
   l=0
   for lists in range(len(total)):
    l=total.count(total[lists])
    l=0 if l==1 else l
    return l

