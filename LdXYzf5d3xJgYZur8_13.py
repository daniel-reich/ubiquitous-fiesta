
def longest_time(h, m, s):
    
    return (h, m, s)[[h * 60 * 60 , m * 60, s].index(max(h * 60 * 60 , m * 60, s))]

