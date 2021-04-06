
def resist_in(data):
    if isinstance(data, tuple): #serialize
        current_value = 0
        for ele in data:
            #print("type:", type(ele))
            if isinstance(ele, float) or isinstance(ele, int):
                temp_value = ele
            else:
                temp_value = resist_in(ele)
            current_value = current_value + temp_value
    else: #parallel
        current_value = 0
        for ele in data:
            if isinstance(ele, float) or isinstance(ele, int):
                temp_value = 1.0/ele
            else:
                temp_value = 1.0/resist_in(ele)
            current_value = current_value + temp_value
        current_value = 1.0/current_value
    
    current_value = round(current_value, 1)
    return current_value
​
def resist(terms):
    import ast
    data = ast.literal_eval(terms)
    #print(type(data))
    value = resist_in(data) 
    
    return value

