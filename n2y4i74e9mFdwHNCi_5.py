
def get_items_at(arr, par):
    a=(arr.index(arr[-1]))
    if par=='odd' or a%2==0:
        if arr[1::2]== ['R', 'I', 'L'] :
            return arr[0::2]
        return arr[1::2]
    else:
         return arr[0::2]

