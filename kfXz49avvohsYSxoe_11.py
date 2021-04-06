
def binary_search(lst, left, right, elem):
    if left>right:
        return False
    mid = left+ (right-left)//2
    if elem==lst[mid]:
        return True
    elif elem < lst[mid]:
        return binary_search(lst,left,mid-1,elem)
    elif elem > lst[mid]:
        return binary_search(lst,mid+1,right,elem)

