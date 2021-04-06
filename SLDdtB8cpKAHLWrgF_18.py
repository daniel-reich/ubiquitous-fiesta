
import re
def greater_permutation(express, num_list):
    permutaions = []
    length = 3
    max_result = 0
    result_str = ""
    for i in range(3):
        ele = []
        temp1 = num_list.copy()
        first = temp1.pop(i)
        for j in range(2):
            temp2 = temp1.copy()
            second = temp2.pop(j)
            ele = [first, second, temp2[0]]
            permutaions.append(ele)
    
    for ele in permutaions:
        temp_express = re.sub('a', str(ele[0]),express)
        temp_express = re.sub('b', str(ele[1]),temp_express)
        temp_express = re.sub('c', str(ele[2]),temp_express)
        
        temp_result = eval(temp_express)
        if temp_result >= max_result:
            max_result = temp_result
            max_result = round(max_result,2)
            if max_result == 0:
                max_result = int(0)
            result_str = temp_express + " = " + str(max_result)
    result_str = result_str.rstrip('0').rstrip('.') if '.' in result_str else result_str
    return result_str

