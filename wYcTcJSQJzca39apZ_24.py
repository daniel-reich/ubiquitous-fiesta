
def truncate(txt, length):
    if length > len(txt):
        return txt
    else:
        a = 0
        for x in range(length, 0, -1):        
            if txt[x] == chr(32):
                a = x
                break
        return txt[:a]

