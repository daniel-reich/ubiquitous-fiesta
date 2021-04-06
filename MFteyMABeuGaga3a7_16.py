
def color_pattern_times(cols):
    duration = len(cols)*2
    for i in range(0,len(cols)-1):
        if cols[i] != cols[i+1]:
            duration += 1
    return(duration)

