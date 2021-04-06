
def soroban(frame):
    countable_rows=[0,4,5,6,7]
    frame=[w.replace('O',"0") for w in frame]
    frame=[w.replace('|',"1") for w in frame]
    val=0
    for r in countable_rows:
        if r == 0:
            for i in range(7):
                val+=int(frame[r][i])*5*(10**(6-i))
        else:
            for i in range(7):
                val+=int(frame[r][i])*(r-3)*(10**(6-i))
    return val

