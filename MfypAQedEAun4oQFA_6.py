
def perrin(n):
 list = [3,0,2]
 for listIndex in range(3, n+1):
    list.append( list[listIndex-3] + list[listIndex-2] )
 return list[n]

