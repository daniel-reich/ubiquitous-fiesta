
def ones_infection(arr):
    z,n=len(arr[0]),len(arr)
    rows=[x for x in range(len(arr)) for y in range(z) if arr[x][y]==1]
    cols=[y for x in range(len(arr)) for y in range(z) if arr[x][y]==1]
    for x in range(len(arr)):
        lst1=[]
        for y in range(z):
            if x in rows or y in cols:
                lst1.append(1)
            if x not in rows and y not in cols:
                lst1.append(0)
        arr.append(lst1)
    for m in range(n) :
        arr.pop(0)
    return (arr)

