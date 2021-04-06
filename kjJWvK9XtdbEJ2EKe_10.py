
def sort_array(array):
    sorted_array = array
    print(array)
    while True:
        for i, val in enumerate(array):
            if i == len(array)-1:
                return array
            if val > array[i+1]:
                array[i] = array[i+1]
                array[i+1] = val
                break
    
    return array

