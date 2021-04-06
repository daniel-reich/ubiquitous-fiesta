
def color_pattern_times(lst): 
    b = [lst[0]]
    for i in range(len(lst)):
        if lst[i]!=b[-1]:
            b.append(lst[i])
    return len(b)-1 + len(lst)*2

