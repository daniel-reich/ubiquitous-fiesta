
def clean_up_list(lst):
    ans = [[],[]]
    for i in lst:
        if int(i) % 2 == 0:
            ans[0].append(int(i))
        else:
            ans[1].append(int(i))
    return ans

