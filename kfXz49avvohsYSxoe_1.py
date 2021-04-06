
def binary_search(arr, left, right, target):
    if left>right: return False
    mid = (left+right)//2
    if target < arr[mid]:
        return binary_search(arr, left, mid-1, target)
    if target > arr[mid]:
        return binary_search(arr, mid+1, right, target)
    return True

