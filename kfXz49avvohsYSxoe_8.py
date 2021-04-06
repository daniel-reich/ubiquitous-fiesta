
def binary_search(arr, left, right, elem):
    if right >= left:
        middle = (left+right)//2
​
        if arr[middle] == elem:
            return True
​
        elif arr[middle] > elem:
            return binary_search(arr, left, middle-1, elem)
        else:
            return binary_search(arr, middle + 1, right, elem)
    else:
        return False

