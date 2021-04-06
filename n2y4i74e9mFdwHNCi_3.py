
def get_items_at(arr, par):
    ans = []
    match = {0:'even',1:'odd'}
    if len(arr)==1:
        if par=='odd':
            ans.append(arr[0])
    else:
        if par==match[len(arr)%2]:
            ans.append(arr[0])
        ans.extend(get_items_at(arr[1:],par))
    return ans

