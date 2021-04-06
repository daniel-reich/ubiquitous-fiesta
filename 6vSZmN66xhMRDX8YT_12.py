
def advanced_sort(lst):
    final_list=[]
    for val in lst:
        count=lst.count(val)
        new_list=[val for i in range(count)]
        if new_list not in final_list:
            final_list.append(new_list)
    return final_list

