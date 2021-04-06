
def nearest_element(num,lst):
    lst1 = [abs(num-a) for a in lst];item= min(lst1)
    indexes = [i for i,a in enumerate(lst1) if a==item]
    final_num = max([lst[a] for a in indexes])
    return lst.index(final_num)

