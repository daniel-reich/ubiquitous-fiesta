
def possible_path(lst):
    return all('H'==lst[i] for i in range(0,len(lst),2)) or all('H'==lst[i] for i in range(1,len(lst),2))

