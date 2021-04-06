
def diag_dom(lst):
    lst=eval(''.join(c for c in str(lst) if c!='-'))
    for i in range(len(lst)):
        main = lst[i].pop(i)
        if main<=sum(lst[i]):
            return False
    return True

