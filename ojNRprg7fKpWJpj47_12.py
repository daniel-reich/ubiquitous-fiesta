
def shift_sentence(txt):
    lst = txt.split(' ')
    arr = []
    for i in lst:
        arr.append(i[0])
​
    arr_new = arr.copy()
    for i in range(len(arr)):
        if i != (len(arr)-1):
            arr_new[i+1] = arr[i]
        else:
            arr_new[0] = arr[i]
    
    print(arr_new)
    result = ''
    count = 0
    for i in arr:
        if count == 0:
            result = result + arr_new[count] + lst[count][1:]
        else:
            result = result + ' ' + arr_new[count] + lst[count][1:]
        count += 1
    
    return result

