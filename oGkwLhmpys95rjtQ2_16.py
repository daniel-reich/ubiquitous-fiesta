
def match_last_item(lst):
    st = ""
    for i in range(len(lst)-1):
        st += str(lst[i])
    return st == lst[-1]

