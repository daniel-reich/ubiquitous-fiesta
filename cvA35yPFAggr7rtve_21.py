
from itertools import permutations
​
def last_ancestor(folders, X, Y):
​
    keysMaster = list(folders.keys())
    length = len(keysMaster)
    perms = permutations(keysMaster)
    keys = []
    for keys in perms:
        stk = [keys[0]]
        testList = [keys[0]]
        while(len(stk) > 0):
            stkKey = stk.pop()
            keyList = folders.get(stkKey, None)
            for lstKey in keyList:
                testKey = folders.get(lstKey, None)
                if(testKey != None):
                    stk.append(lstKey)
                    testList.append(lstKey)
        if(len(testList) == length):
            break
        
    paths = []
    targets = [X, Y]
    for index in range(len(targets)):
        iters = []
        path = []
        it = iter(keys)
        iters.append(it)
        path.append(keys[0])
        done = False
        while len(iters) > 0:
            it = iters[len(iters) - 1]
            try:
                while True:
                    i = next(it)
                    if(i == targets[index]):
                        if(i not in path):
                            path.append(i)
                        done = True
                        break
                    lst = folders.get(i, None)
                    if(lst != None):
                        it = iter(lst)
                        iters.append(it)
                        if(i not in path):
                            path.append(i)
                        break
            except:
                it = iters.pop()
                path.pop()
            if(done):
                break
        paths.append(path)
        
    res = []
    for node in paths[0]:
        if(node in paths[1]):
           res.append(node)
           
    return res[len(res) - 1]

