
def balanced(input_array):
    if sum(input_array[0:int(len(input_array)/2):1]) > sum(input_array[int(len(input_array)/2):len(input_array):1]):
        return input_array[0:int(len(input_array)/2):1] + input_array[0:int(len(input_array)/2):1]
    elif sum(input_array[0:int(len(input_array)/2):1]) < sum(input_array[int(len(input_array)/2):len(input_array):1]):
        return input_array[int(len(input_array) / 2):len(input_array):1] + input_array[int(len(input_array) / 2):len(input_array):1]
    else:
        return input_array

