
def find_fulcrum(lst):
    for i in range(1,len(lst)):
        if i!=(len(lst)-1):
            n1 = lst[:i]
            n2 = lst[i+1:]
            if sum(n1) == sum(n2):
                print(n1)
                print(n2)
                return lst[i]
                break
            else:
                pass
        else:
            return -1

