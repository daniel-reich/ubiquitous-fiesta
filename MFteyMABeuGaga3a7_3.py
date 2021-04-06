
def color_pattern_times(cols):
    colouring = 2 * len(cols)
    switching = sum(1 for i in range(len(cols)-1) if cols[i] != cols[i+1])
    return colouring + switching

