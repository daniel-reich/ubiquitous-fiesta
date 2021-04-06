
def longest_run(lst):
    def front_back(lst):
        l, n = list(), list()
        for i in range(len(lst)-1):
            if lst[i]+1 == lst[i+1]:
                n.append(lst[i])
            else:
                n.append(lst[i])
                l.append(len(n))
                n=[]
        l.append(len(n)+1)
        print(l)
        return max(l)
    return max(front_back(lst),front_back(lst[::-1]))

