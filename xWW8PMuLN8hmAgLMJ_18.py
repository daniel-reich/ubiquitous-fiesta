
import operator as o
​
def postfix(ex):
    s ={'+' : o.add,'-' : o.sub,'*' : o.mul, '/' : o.truediv}; n = ex.split()
    while len(n) > 1:
        for i in n:
            if not i[-1].isnumeric():
                p=n.index(i)
                n.insert(p-2,str(int(s[n.pop(p)](int(n.pop(p-2)),int(n.pop(p-2))))))
                break
    return int(float((n[0])))

