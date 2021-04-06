
def next_letters(text):
    newnbrs = []
    inc = 1
    for nbr in list(map (lambda x: ord(x),text.upper()[::-1])):
        newnbr =  nbr + inc
        inc = 0
        if  newnbr > ord("Z"):
            newnbr = ord("A")
            inc = 1
        newnbrs.append(newnbr)
    if inc == 1:
        newnbrs.append(ord("A"))
   
    return "".join(list(map (lambda x: chr(x),newnbrs)))[::-1]

