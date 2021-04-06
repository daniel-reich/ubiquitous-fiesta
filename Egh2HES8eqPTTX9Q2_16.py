
def rolling_cipher(txt, n):
    import string
    from collections import deque
    
    intab = string.ascii_lowercase
    q = deque(list(string.ascii_lowercase))
    q.rotate(-n)
    outtab = ''.join(list(q))
    trantab = str.maketrans(intab, outtab)
    return(txt.translate(trantab))

