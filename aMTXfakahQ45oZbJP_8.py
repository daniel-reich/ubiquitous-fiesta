
def complete_bracelet(lst):
    for i in range(2, 1+len(lst)//2):
        if len(lst)%i == 0:
            for k in range(i, len(lst), i):
                if lst[:i] != lst[k:k+i]:
                    break
                return True
    return False

