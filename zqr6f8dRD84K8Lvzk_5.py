
def hex_lattice(n):
​
    def create_recur(end, level=0):
        if level < end:
            return (end-level+1)*' '+(end+1+level)*'o '+(end-level)*' '+'\n'+create_recur(end, level + 1)+(end-level+1)*' '+(end+1+level)*'o '+(end-level)*' '+'\n'
        elif level == end:
            return ' '+(end+1+level)*'o '+'\n'
        return ''
​
    nth = (3 + (12*n - 3)**0.5)/6
    if nth*10 % 10 != 0:
        return 'Invalid'
    nth = int(nth) - 1
    return create_recur(nth)[:-1]

