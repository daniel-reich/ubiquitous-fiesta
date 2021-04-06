
def pyramidal_string(string, _type='REG'):
    numrows = ((8*len(string) +1)**0.5 -1)/2
    if not numrows.is_integer(): return 'Error!'
    if _type=='REV': 
        return [row[::-1] for row in pyramidal_string(string[::-1])][::-1]
    return [' '.join(string[sum(range(i)):sum(range(i+1))])
            for i in range(1, int(numrows)+1)]

