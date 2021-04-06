
def format_num(n):
    s_n = str(n)
    
    for i in range(len(s_n),0,-3):
        s_n = s_n[:i] + ',' + s_n[i:]
    
    return s_n[:len(s_n)-1]

