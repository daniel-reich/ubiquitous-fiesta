
def setify(lst):
        c=[]
        b=set()
        for i in lst:
                b.add(i)
        for j in b:
                c.append(j)
        c.sort()
        return c
​
setify([1, 3, 3, 5, 5]) 
​
setify([4, 4, 4, 4]) 
​
setify([5, 7, 8, 9, 10, 15]) 
​
setify([3, 3, 3, 2, 1])

