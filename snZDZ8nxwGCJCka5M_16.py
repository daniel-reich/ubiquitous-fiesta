
def pyramidal_string(string, typ):
    if not is_possible(len(string)):
        return 'Error!'
    items = 1
    ans = []
    row = ''
    while string:
        for i in range(items):
            if typ == 'REV':
                row = string[-1] + row
                string = string[:-1]
            else:
                row += string[0]
                string = string[1:]
        ans.append(' '.join(row))
        row = ''
        items += 1
    if typ == 'REV':
        return ans[::-1]
    return ans               
     
def is_possible(los): 
    tot = 0
    n = 1
    while(tot < los): 
        tot += n 
        n += 1
    return tot == los

