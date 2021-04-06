
def char_at_pos(input, position):
    if position == "even":
        result = [input[i] for i in range(1, len(input), 2)]
    elif position == "odd":
        result = [input[i] for i in range(0, len(input), 2)]        
    else:
        return
    
    if type(input) == str:
        return ''.join(result)
​
    return result

