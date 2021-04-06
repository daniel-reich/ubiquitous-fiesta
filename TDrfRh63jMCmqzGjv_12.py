
def is_anti_list(a,b):
    for x in a:
        if x not in b:
            return False
        else:
            lst = []
            for x in range(len(a)):
                if a[x] != b[x]:
                    lst.append(True)
                else:
                    lst.append(False)
            return all(lst)

