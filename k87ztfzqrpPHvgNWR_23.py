
def widen_streets(lst, n):
    t = list(zip(*lst))                                          # t = transposed
    w = [row if set(row) != {' '} else [row]*n for row in t]      # w = widened
​
    output = []                                             
    for i in w:                                                  #removing nested lists
        if type(i) == list:
            for x in i:
                output.append(x)
        else:
            output.append(i)
            
    result = list(zip(*output))                                  #transposing again
    return [''.join(i) for i in result]

