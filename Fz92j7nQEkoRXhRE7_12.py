
def jumping_frog(n, stones):
    tested,to_test,n=[],[0],0
    while len(to_test)>0:
        n+=1
        for elem in to_test[:]:
            if elem+stones[elem]>=len(stones):
                return n+1
            if elem+stones[elem] not in tested and elem+stones[elem]<len(stones):
                to_test.append(elem+stones[elem])
            if elem-stones[elem] not in tested and elem-stones[elem]>0:
                to_test.append(elem-stones[elem])
            
            tested.append(elem)
            to_test.remove(elem)
    return "no chance :-("

