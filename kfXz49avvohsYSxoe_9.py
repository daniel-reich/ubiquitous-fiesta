
def binary_search(thelist,left,right,targetvalue):
    left = 0
    right = int(len(thelist)-1)
    while left <= right:
        if thelist[((left+right)//2)] < targetvalue:
           left = (((left+right)//2)+1)
        elif thelist[((left+right)//2)] == targetvalue:
           return True
        else:
           right =(((left+right)//2)-1)
    return False

