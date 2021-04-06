
def number_groups(group1, group2, group3):
    lst1=[]
    lst1.extend(list(set(group1)&set(group3))),lst1.extend(list(set(group1)&set(group2))),lst1.extend(list(set(group2)&set(group3)))    
    return(sorted(list(set(lst1))))

