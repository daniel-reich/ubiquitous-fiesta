
def generate_nonconsecutive(n):
    l=""
    for i in range(0, 2**n) :
        if bin(i).find("11")>-1 :
            continue
        l+=" "+bin(i).replace("0b", "").zfill(n)
    return l.strip()

