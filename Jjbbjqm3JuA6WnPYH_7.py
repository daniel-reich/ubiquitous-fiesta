
def bit_rotate(n, m, d):
    string= bin(n).replace("0b","")
    if len(string)<m:
        m=m-len(string)
    return int(string[m-2*m*d:] + string[:m-2*m*d],2)

