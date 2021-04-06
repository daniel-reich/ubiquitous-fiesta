
def get_items_at(arr, par):
    if par == "even": 
        arr.pop()
    return get_items_2(arr,[],True)
def get_items_2(arr,result,command=True):
    if command == True:
        result = [arr[-1]] + result
        if len(arr) == 1: return result
        return get_items_2(arr[0:-1],result,command=False)
    elif command == False:
        if len(arr) == 1: return result
        return get_items_2(arr[0:-1],result,command=True)

